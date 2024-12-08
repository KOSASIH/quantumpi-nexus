// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Governance is Ownable {
    struct Proposal {
        string description;
        uint256 voteCount;
        uint256 endTime;
        bool executed;
    }

    IERC20 public token;
    Proposal[] public proposals;
    mapping(uint256 => mapping(address => bool)) public votes;

    event ProposalCreated(uint256 indexed proposalId, string description, uint256 endTime);
    event Voted(uint256 indexed proposalId, address indexed voter);
    event ProposalExecuted(uint256 indexed proposalId);

    constructor(IERC20 _token) {
        token = _token;
    }

    function createProposal(string memory description, uint256 duration) external onlyOwner {
        uint256 endTime = block.timestamp + duration;
        proposals.push(Proposal({
            description: description,
            voteCount: 0,
            endTime: endTime,
            executed: false
        }));
        emit ProposalCreated(proposals.length - 1, description, endTime);
    }

    function vote(uint256 proposalId) external {
        require(proposalId < proposals.length, "Proposal does not exist");
        require(block.timestamp < proposals[proposalId].endTime, "Voting has ended");
        require(!votes[proposalId][msg.sender], "Already voted");

        votes[proposalId][msg.sender] = true;
        proposals[proposalId].voteCount += token.balanceOf(msg.sender);
        emit Voted(proposalId, msg.sender);
    }

    function executeProposal(uint256 proposalId) external {
        require(proposalId < proposals.length, "Proposal does not exist");
        require(block.timestamp >= proposals[proposalId].endTime, "Voting has not ended");
        require(!proposals[proposalId].executed, "Proposal already executed");

        proposals[proposalId].executed = true;
        // Execute proposal logic here (e.g., change state, transfer funds, etc.)
        emit ProposalExecuted(proposalId);
    }
}
