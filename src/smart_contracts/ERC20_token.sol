// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract AdvancedERC20 is ERC20, Ownable, Pausable {
    mapping(address => bool) private _minters;
    mapping(address => bool) private _burners;

    event MinterAdded(address indexed account);
    event MinterRemoved(address indexed account);
    event BurnerAdded(address indexed account);
    event BurnerRemoved(address indexed account);

    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    modifier onlyMinter() {
        require(_minters[msg.sender], "Caller is not a minter");
        _;
    }

    modifier onlyBurner() {
        require(_burners[msg.sender], "Caller is not a burner");
        _;
    }

    function addMinter(address account) external onlyOwner {
        _minters[account] = true;
        emit MinterAdded(account);
    }

    function removeMinter(address account) external onlyOwner {
        _minters[account] = false;
        emit MinterRemoved(account);
    }

    function addBurner(address account) external onlyOwner {
        _burners[account] = true;
        emit BurnerAdded(account);
    }

    function removeBurner(address account) external onlyOwner {
        _burners[account] = false;
        emit BurnerRemoved(account);
    }

    function mint(address to, uint256 amount) external onlyMinter {
        _mint(to, amount);
    }

    function burn(uint256 amount) external onlyBurner {
        _burn(msg.sender, amount);
    }

    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    function _beforeTokenTransfer(address from, address to, uint256 amount) internal whenNotPaused override {
        super._beforeTokenTransfer(from, to, amount);
    }
}
