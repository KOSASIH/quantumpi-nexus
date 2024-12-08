// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract YieldFarming is Ownable {
    IERC20 public stablecoin; // The stablecoin used for staking
    uint256 public rewardRate; // Reward rate in basis points (e.g., 100 for 1%)

    struct Stake {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt for the user
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes
    uint256 public totalStaked; // Total amount staked in the contract

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    constructor(IERC20 _stablecoin, uint256 _rewardRate) {
        stablecoin = _stablecoin;
        rewardRate = _rewardRate; // Set the reward rate
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.rewardDebt += calculatePendingReward(msg.sender); // Update reward debt before changing the stake
        userStake.amount += amount;

        totalStaked += amount; // Update total staked amount
        stablecoin.transferFrom(msg.sender, address(this), amount); // Transfer tokens to the contract

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        userStake.rewardDebt += calculatePendingReward(msg.sender); // Update reward debt before changing the stake
        userStake.amount -= amount;

        totalStaked -= amount; // Update total staked amount
        stablecoin.transfer(msg.sender, amount); // Transfer tokens back to the user

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimReward() external {
        uint256 reward = calculatePendingReward(msg.sender);
        require(reward > 0, "No rewards available");

        stakes[msg.sender].rewardDebt += reward; // Update reward debt
        stablecoin.transfer(msg.sender, reward); // Transfer rewards to the user

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate pending rewards for a user
    function calculatePendingReward(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        return (userStake.amount * rewardRate) / 10000; // Calculate reward based on staked amount and reward rate
    }

    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
