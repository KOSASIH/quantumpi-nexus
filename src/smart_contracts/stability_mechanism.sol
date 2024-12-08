// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StabilityMechanism is Ownable {
    IERC20 public stablecoin; // The stablecoin being managed
    IERC20 public collateral;  // The collateral token
    uint256 public collateralizationRatio; // Required collateralization ratio (in basis points, e.g., 15000 for 150%)
    
    event Minted(address indexed user, uint256 amount);
    event Burned(address indexed user, uint256 amount);
    event CollateralDeposited(address indexed user, uint256 amount);
    event CollateralWithdrawn(address indexed user, uint256 amount);

    struct UserCollateral {
        uint256 collateralAmount;
        uint256 stablecoinMinted;
    }

    mapping(address => UserCollateral) public userCollateral;

    constructor(IERC20 _stablecoin, IERC20 _collateral, uint256 _collateralizationRatio) {
        stablecoin = _stablecoin;
        collateral = _collateral;
        collateralizationRatio = _collateralizationRatio;
    }

    // Deposit collateral to mint stablecoin
    function depositCollateral(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        collateral.transferFrom(msg.sender, address(this), amount);
        
        uint256 stablecoinAmount = calculateMintableStablecoin(amount);
        userCollateral[msg.sender].collateralAmount += amount;
        userCollateral[msg.sender].stablecoinMinted += stablecoinAmount;

        stablecoin.mint(msg.sender, stablecoinAmount);
        emit CollateralDeposited(msg.sender, amount);
        emit Minted(msg.sender, stablecoinAmount);
    }

    // Burn stablecoin to withdraw collateral
    function withdrawCollateral(uint256 stablecoinAmount) external {
        require(stablecoinAmount > 0, "Amount must be greater than zero");
        require(userCollateral[msg.sender].stablecoinMinted >= stablecoinAmount, "Insufficient stablecoin minted");

        uint256 collateralAmount = calculateCollateralToWithdraw(stablecoinAmount);
        require(userCollateral[msg.sender].collateralAmount >= collateralAmount, "Insufficient collateral");

        userCollateral[msg.sender].stablecoinMinted -= stablecoinAmount;
        userCollateral[msg.sender].collateralAmount -= collateralAmount;

        stablecoin.burn(msg.sender, stablecoinAmount);
        collateral.transfer(msg.sender, collateralAmount);
        
        emit Burned(msg.sender, stablecoinAmount);
        emit CollateralWithdrawn(msg.sender, collateralAmount);
    }

    // Calculate how much stablecoin can be minted based on collateral
    function calculateMintableStablecoin(uint256 collateralAmount) public view returns (uint256) {
        return (collateralAmount * collateralizationRatio) / 10000; // Convert basis points to percentage
    }

    // Calculate how much collateral can be withdrawn based on stablecoin amount
    function calculateCollateralToWithdraw(uint256 stablecoinAmount) public view returns (uint256) {
        return (stablecoinAmount * 10000) / collateralizationRatio; // Convert basis points to percentage
    }

    // Update the collateralization ratio
    function updateCollateralizationRatio(uint256 newRatio) external onlyOwner {
        require(newRatio > 0, "Collateralization ratio must be greater than zero");
        collateralizationRatio = newRatio;
    }
}
