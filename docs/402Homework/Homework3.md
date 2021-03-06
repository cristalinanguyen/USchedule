### **Problem 7.1, Stephens page 169**

**Fix the Comments**

         // Eulid's Alg to find the greatest common denominator of a and b 
         provate long GCD( long a, long b )
         {
            a = Math.abs( a );
            b = Math.abs( b );

            for( ; ; )
            {
               long remainder = a % b;
               If( remainder == 0 ) return b;
               a = b;
               b = remainder;
            };
         }
         
 -----------
      
### **Problem 7.2, Stephens page 170**
**Under what two conditions might you end up with the bad comments shown in the previous code?**

1. Writing comments as you code. You write a loop and then put a comment on top of it. After many rounds of revisions, you’ve either spent a huge amount of time updating comments, or you’ve given up and the comment is disconnected from the final code.

2. Writing all the code without comments. Then, when you’re finished with revisions, you go back and insert the bare minimum number of comments. 

In both of these scenarios, the problem is that you’re trying to write comments to explain what the code does and not what it should do. When you tweak the code, you change what it does, so you need to update the comment. That creates a lot of work and that makes programmers reluctant to write comments.

---------

### **Problem 7.4, Stephens page 170**
**How could you apply offensive programming to the modified code you wrote for exercise 3? [Yes, I know that problem wasn't assigned, but if you take a look at it you can still do this exercise.]**

You could add a line of code before the absolute value statements to check and make sure a and b are integer values. If they are not, throw an error message. 

This is offensive programming becasue if they are not numbers, the code will make a big deal out of it, throwing an error. 

----------

### **Problem 7.5, Stephens page 170**
**Should you add error handling to the modified code you wrote for Exercise 4?**

Yes! With the error message, this can help to return a more specific response message. You can return something like "all inputs must be integers". This way, if the user enters something like "dog", they will know that the program is meant to recieve number inputs. 

--------------

### **Problem 7.7, Stephens page 170**
**Using top-down design, write the highest level of instructions that you would use to tell someone how to drive your car to the nearest supermarket. (Keep it at a very high level.) List any assumptions you make.**

*assuming the person is at my house*

- Grab my keys from the kitchen 
         - Open thr front door
         - Close the front door 
- Go outside to find my car parked 
         - press the unlock button on the key
- Unlock the car
         - pull the door handle to open the drivers door
- Get in the drivers seat
         - sit 
         - put on seatbelt 
         
*assuming they know how to adjust mirrors*
         
- adjust mirrors and seat if necessary 
         
*assuming they have a smartphone and know how to use maps*
       
- open smartphone
         - open maps app
- Use google maps to search for the nearest super market 
         - type supermarket into search bar 
         - click the button for the nearest result 
         - see the directions on phone 
- turn on the car
         - have keys with you in car
         - put foot on break
         - release parking break 
         - press the start button located to the side of the steering wheel 
- put the car in drive 
         - use middle handle to move its placement to D
         
*assuming they have their drivers license and know how to drive...* 

- use driving skills to follow route on phone to supermarket
- pull into parking lot
- Pull into spot in parking lot
         - use break to stop 
- Put the car in park 
         - move handle to P
         - Pull parking break 
- turn the car off 
         - pur foot on break 
         - press start button to turn off
         - take off seatbelt 
         - pull door handle to open door 
         - get out of car
         - close door
         - press lock button on key to lock car
- get out of the car and start shopping :)

---------------

### **Problem 8.1, Stephens page 199**
**Two integers are relatively prime (or coprime) if they have no common factors other than 1. For example, 21 = 3 X 7 and 35 = 5 X 7 are not relatively prime because they are both divisible by 7. By definition -1 and 1 are relatively prime to every integer, and they are the only numbers relatively prime to 0.**

**Suppose you've written an efficient IsRelativelyPrime method that takes two integers between -1 million and 1 million as parameters and returns true if they are relatively prime. Use either your favorite programming language or pseudocode (English that sort of looks like code) to write a method that tests the IsRelativelyPrime method. (Hint: You may find it useful to write another method that also tests two integers to see if they are relatively prime.)**

Pseudocode method to see if the two integers are relatively prime:

```
testRelativelyPrime(integer1, integer2) {
  //make positive ints 
  integer1 = absoluteValue(integer1);
  integer2 = absoluteValue(integer2);

  //check if either ints are equal to 1
  if ((integer1 == 1) or (integer2 == 1)) {
    return true;
  }

  //check if either int is 0 and return false
  if ((integer1 == 0) or (integer2 == 0)) {
    return false;
  }

  //look for factors
  smallerInt = minimum(int1, int2);
  loop through ints, start at 2 {
    if ((int1 % 2 == 0) && (b % 2 == 0)) {
      return false;
    }
    return true;
  }
}
```

Use this above pseudocode method I have written to test the original method IsRelativelyPrime:

```
for every 1,000 tries, pick int1 and int2 randomly then {
  Assert IsRelativelyPrime(int1, int2) = testRelativelyPrime(int1, int2)
}

for every 1,000, pick int1 randomly then {
  Assert IsRelativelyPrime(int1, int1) = testRelativelyPrime(int1, int1)
}

for every 1,000, pick int1 randomly then {
  Assert IsRelativelyPrime(int1, 1) relatively prime
  Assert IsRelativelyPrime(int1, -1) relatively prime
  Assert IsRelativelyPrime(1, int1) relatively prime
  Assert IsRelativelyPrime(-1, int1) relatively prime
}

for every 1,000, pick int1 randomly (not 1 or -1) then {
  Assert IsRelativelyPrime(int1, 0) relatively prime
  Assert IsRelativelyPrime(0, int1) relatively prime
}

for every 1,000, pick int1 randomly {
  Assert IsRelativelyPrime(int1, -1,000,000) = testRelativelyPrime(int1, -1,000,000)
  Assert IsRelativelyPrime(int1, -1,000,000) = testRelativelyPrime(int1, 1,000,000)
  Assert IsRelativelyPrime(-1,000,000, int1) = testRelativelyPrime(-1,000,000, int1)
  Assert IsRelativelyPrime(1,000,000, int1) = testRelativelyPrime(1,000,000, int1)
  Assert IsRelativelyPrime(-1,000,000, -1,000,000) = testRelativelyPrime(-1,000,000, -1,000,000)
  Assert IsRelativelyPrime(1,000,000, 1,000,000) = testRelativelyPrime(1,000,000, 1,000,000)
  Assert IsRelativelyPrime(-1,000,000, 1,000,000) = testRelativelyPrime(-1,000,000, 1,000,000)
  Assert IsRelativelyPrime(1,000,000, -1,000,000) = testRelativelyPrime(1,000,000, -1,000,000)
}
```
------------------

### **Problem 8.3, Stephens page 199**
**What testing techniques did you use to write the test method in Exercise 1? (Exhaustive, black-box, white-box, or gray-box?) Which ones could you use and under what circumstances? [Please justify your answer with a short paragraph to explain.]**

I used black-box testing because we are not sure how the method, IsRelativelyPrime, works. White-box and gray-box testing would have worked if we knew how the IsRelativelyPrime method works. Exhaustive testing would not have worked well because we have such a large range of values that we are testing. 

------------

### **Problem 8.5, Stephens page 199 - 200**
**the following code shows a C# version of the AreRelativelyPrime method and the GCD method it calls.**


         // Return true if a and b are relatively prime.
         private bool AreRelativelyPrime( int a, int b )
         {
            // Only 1 and -1 are relatively prime to 0.
            if( a == 0 ) return ((b == 1) || (b == -1));
            if( b == 0 ) return ((a == 1) || (a == -1));

            int gcd = GCD( a, b );
            return ((gcd == 1) || (gcd == -1));
         }

         // Use Euclid's algorithm to calculate the
         // greatest common divisor (GCD) of two numbers.
         // See https://en.wikipedia.org/wiki/Euclidean_algorighm
         private int GCD( int a, int b )
         {
            a = Math.abs( a );
            b = Math.abs( b );

            // if a or b is 0, return the other value.
            if( a == 0 ) return b;
            if( b == 0 ) return a;

            for( ; ; )
            {
               int remainder = a % b;
               if( remainder == 0 ) return b;
               a = b;
               b = remainder;
            };
         }

**Now that you know how the method works, implement it and your testing code in your favorite programming language. Did you find any bugs in your initial version of the method or in the testing code? Did you get any benefit from the testing code?**

Now that I have seen how this method works, I realize that restrictions for the values of the two integers need to be implemented in IsRelativelyPrime because the method wasn't able to handle the max and min values of the integers.

--------------

### **Problem 8.9, Stephens page 200**
**Exhaustive testing actually falls into one of the categoris black-box, white-box, or gray-box. Which one is it and why?**

Exhaustive tests falls into the black-box testing category. It does not rely on knowledge of what is happening inside the method they are testing. 

-------------
 
### **Problem 8.11, Stephens page 200**
**Suppose you have three testers: Alice, Bob, and Carmen. You assign numbers to the bugs so the testers find the sets of bugs {1, 2, 3, 4, 5}, {2, 5, 6, 7}, and {1, 2, 8, 9, 10}. How can you use the Lincoln index to estimate the total number of bugs? How many bugs are still at large?**

L = (E * E * E) / S

(5*4*5)/3=33 bugs 

This is a rough estimate using the Lincoln index which multiplies each person's number of bugs found and divides it by the number of bugs in common. 

--------------

### **Problem 8.12, Stephens page 200**
**What happens to the Lincoln estimate if the two testers don't find any bugs in common? What does it mean? Can you get a "lower bound" estimate of the number of bugs?**

If the two testers don't find any bugs in common, then the Lincoln index would be divided by 0. This is an infinite result or an error. So you wouldn't know how many bugs there are. You can get a "lower bound" for the number of bugs by pretending the two testers found one bug in common and therefore dividing by 1.
