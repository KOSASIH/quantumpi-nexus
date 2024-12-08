// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract InsuranceProtocol is Ownable {
    IERC20 public stablecoin; // The stablecoin used for insurance payments

    struct Policy {
        uint256 premium;
        uint256 coverageAmount;
        bool isActive;
    }

    mapping(address => Policy) public policies;

    event PolicyPurchased(address indexed user, uint256 premium, uint256 coverageAmount);
    event PolicyClaimed(address indexed user, uint256 amount);

    constructor(IERC20 _stablecoin) {
        stablecoin = _stablecoin;
    }

    function purchasePolicy(uint256 coverageAmount) external {
        require(coverageAmount > 0, "Coverage amount must be greater than zero");
        uint256 premium = calculatePremium(coverageAmount);

        stablecoin.transferFrom(msg.sender, address(this), premium);
        policies[msg.sender] = Policy(premium, coverageAmount, true);

        emit PolicyPurchased(msg.sender, premium, coverageAmount);
    }

    function claimPolicy() external {
        Policy storage policy = policies[msg.sender];
        require(policy.isActive, "No active policy found");

        stablecoin.transfer(msg.sender, policy.coverageAmount);
        policy.isActive = false; // Mark policy as claimed

        emit PolicyClaimed(msg.sender, policy.coverageAmount);
    }

    function calculatePremium(uint256 coverageAmount) internal pure returns (uint256) {
        return (coverageAmount * 5) / 100; // Example: 5% premium
    }
}
