# Understanding the file
What I do here is pretty simple, I just went out to check my trust on Proof of Work system, so I myselves, try to come up with a number, or "mine" such number so that it starts with 3 zeros
to begin with.
I import Hashlib library that has SHA256 function, take and string input, consider an iterator at the end of string and check whether it begins with several zeroes, and loop it until 
it doesn't.
At the end, I print the number and time in millisecond the code took to find such a number. Even for small begins of 3-4 zeroes, the system takes on average, significant amount of time
 and getting the number is as good as guessing. Thus, we can begin to trust HASH functions. For more details about the inner workings of these functions, one can go on study about them.
 
