# INTRODUCTION
 The project game of blocks was originally offered by *Programming Club, IIT Kanpur* during Summer Camp 2021, and I followed and improved upon the content available there. It got me intrigued and I started to explore the web for learning towards __BlockChain Management__ and how they work. 

Update - 1 : How you make an Blockchain work could be thought of very well, if you start thinking of alleviating the central trusting body and thus, mutual trust on each other by considering the starting example of how the public ledger system would change under the circumstances that you trust no one.


So, firstly there is some public ledger and maybe to sign or **"validate"** some transaction, the one owing money or the one, "paying" money in some arbitrary sense, makes a signature, but it can be copied again and again. So, one comes up with the website version and some online signature sort of thing. To verify that, he is the one who signed when making that transaction, the concept of **public and private keys** must have evolved from there. I am here in the introduction, not getting in the formal workings of the system, but one can think and get assured(by trusting the Supreme Overlord of Cryptographic HASH functions), that one can only make the signature using one's private key and public key along with the signature can be used to verify that transaction. (The signature is an outcome of a function that takes in Message, private key and the current timing or the number of current transaction to produce a unique series of 1s and 0s, that coupled with public key will lead a speical number that ensures security.) Thus, one has formed some trust for the system. But still the one hosting the website is the Centralised authority and to ensure no failure, in him we trust. 

# Proof-of-Work to trust the one
To alleviate this _trust_, what one can do is that everyone makes their own copy of ledger. But then if two copies don't match, whom will you trust. What Blockchains do in such cases is trust the "Blockchain" with largest "Chain". To simplify, some pre-specified number of transaction, is packed as one Block, and it contains "hash" of previous box, after this, the miners try to comeup with a number, on a totally luck basis, that one coupled with transactions list and previous message and fed as an input to SHA-256(different BlockChains used different hash functions, but this one is used the most.), gives up a number starting with several zeros(let's say atleast 30 zeros for demonstration, but the actual length depends on current power of all miners combined so the block is "mined", or the number is found in an average time, predecided.) This system of Trust is known as Proof of Work, as one needs to work a lot to get that hash function that validates the block.


# How Ethereum is different and what needs to be done.
We know that Bitcoin is a cryptocurrency, something which you can use as something of value, sort of like the Indian Rupee or US Dollar. You can use it to buy stuff, and trade something of value. And you might be thinking, well, what is so different in Ethereum that is not there in Bitcoin? Why do we need this another cryptocurrency when Bitcoin suffices in all the aspects of serving as a currency. Well, Bitcoin being just a currency is the exact problem. The world needs more! 

We don't just need to have a decentralized currency, but we also want the world to have decentralized voting, decentralized auctions, decentralized identity management, decentralized asset transferring (most of these are implemented using Game Theoretical concepts, and you are going to implement these towards the end of this project, in solidity!). 

These things are currently done in a centralized way and people don't usually have control over their results, such as Ballot tampering / booth capturing in voting, fraud and collusion with the auctioner in an auction, Facebook sharing your identity with Cambridge analytica, which gets leaked, and Bank frauds... there are countless issues with how they are done currently. 

Having them work in a decentralized way, such that its not just one single party that is aware of the results and actual count, but every single node in the world is aware of the number of votes cast, the auction amount bid, encrypted data stored, and asset transfer made. Having this decentralization of the records remove any possibility of fraud, as every node in the world can prove a fake claim wrong, as they have proof of the actual results of these processes.
Bitcoin, being just a currency, can not do all this. 

Thus we need a decentralized mechanism to perform such tasks. These tasks can, obviously, be modeled as a computer code. 

Thus we need something to execute computer code in a decentralized fashion, essentially forming a World Computer! 

Ethereum aims to do just that. Now you might be thinking that Ethereum also has its own currency, called Ether, ETH. But its main purpose is to incentivize participation of more and more users and nodes in the World Computer, so as to increase the capacity of the world computer! The more transactions, the more blocks mined, the more ETH produced, and more rewards for the participants! 


# Solidity Contracts
Ethereum works by making use of smart contracts, which are code fragments which are publicly available on Ethereum, to ask the nodes to perform a certain task and put its results on the blockchain. How does a smart contract work?...well it can be thought of as a vending machine.
Solidity is used to write such contracts.  Solidity is an object-oriented, contract-oriented, high-level language for implementing smart contracts.
Solidity is statically typed, supports inheritance, libraries and complex user-defined types among other features.

It is possible to create contracts for voting, crowdfunding, blind auctions, multi-signature wallets and more using solidity and we aim to create and understand the implementations of such complex problems.
