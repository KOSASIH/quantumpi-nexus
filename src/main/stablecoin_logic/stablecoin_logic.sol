// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract StablecoinLogic is ERC20, Ownable {
    using SafeMath for uint256;

    uint256 public constant TARGET_VALUE = 314159; // Target value in cents
    uint256 public totalSupplyCap; // Maximum supply cap
    address public priceOracle; // Price oracle address

    event PriceOracleUpdated(address indexed newOracle);
    event SupplyAdjusted(uint256 newSupply);

    constructor(uint256 initialSupply, address _priceOracle) ERC20("QuantumPi Stablecoin", "QPS") {
        totalSupplyCap = initialSupply;
        priceOracle = _priceOracle;
        _mint(msg.sender, initialSupply);
    }

    modifier onlyPriceOracle() {
        require(msg.sender == priceOracle, "Caller is not the price oracle");
        _;
    }

    function updatePriceOracle(address newOracle) external onlyOwner {
        priceOracle = newOracle;
        emit PriceOracleUpdated(newOracle);
    }

    function adjustSupply(uint256 currentPrice) external onlyPriceOracle {
        if (currentPrice < TARGET_VALUE) {
            uint256 amountToMint = (TARGET_VALUE - currentPrice).mul(totalSupply()).div(TARGET_VALUE);
            _mint(address(this), amountToMint);
            emit SupplyAdjusted(totalSupply());
        } else if (currentPrice > TARGET_VALUE) {
            uint256 amountToBurn = (currentPrice - TARGET_VALUE).mul(totalSupply()).div(TARGET_VALUE);
            _burn(address(this), amountToBurn);
            emit SupplyAdjusted(totalSupply());
        }
    }
}
