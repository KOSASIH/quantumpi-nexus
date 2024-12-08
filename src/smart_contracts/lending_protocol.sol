// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LendingProtocol is Ownable {
    IERC20 public stablecoin; // The stablecoin used for lending and borrowing
    uint256 public interestRate; // Interest rate in basis points (e.g., 500 for 5%)

    struct Loan {
        uint256 amount;
        uint256 interest;
        uint256 dueDate;
        bool isActive;
    }

    mapping(address => Loan) public loans;

    event LoanCreated(address indexed borrower, uint256 amount, uint256 interest, uint256 dueDate);
    event LoanRepaid(address indexed borrower, uint256 amount);

    constructor(IERC20 _stablecoin, uint256 _interestRate) {
        stablecoin = _stablecoin;
        interestRate = _interestRate;
    }

    function createLoan(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(loans[msg.sender].isActive == false, "Existing loan must be repaid first");

        uint256 interest = (amount * interestRate) / 10000; // Calculate interest
        uint256 dueDate = block.timestamp + duration;

        loans[msg.sender] = Loan(amount, interest, dueDate, true);
        stablecoin.transfer(msg.sender, amount);

        emit LoanCreated(msg.sender, amount, interest, dueDate);
    }

    function repayLoan() external {
        Loan storage loan = loans[msg.sender];
        require(loan.isActive, "No active loan found");
        require(block.timestamp <= loan.dueDate, "Loan is overdue");

        uint256 totalRepayment = loan.amount + loan.interest;
        stablecoin.transferFrom(msg.sender, address(this), totalRepayment);

        loan.isActive = false; // Mark loan as repaid
        emit LoanRepaid(msg.sender, totalRepayment);
    }

    function updateInterestRate(uint256 newRate) external onlyOwner {
        interestRate = newRate;
    }
}
