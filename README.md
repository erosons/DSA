
### Data Structure is driven by
   -  Big O notation is an algebraic way to express Space and time complexity of a programming process
   -  Big O - Is used to understand time and space complexity , when comparing algorithm that solves the same problem.
   -  O(n) This is a notation to define complexity: O-> Order of magnitude of complexity  (n) -> A function of the size and time
   -  Data structure and Algorithm  practice codes www.AlgoExpert.io
<img height="250" src="https://github.com/erosons/DSA/blob/main/images/1636528337192.png" />
  
  
### Algorithm 
---------------
Are set of step/approach used to solve particular task/problem

  Key Components that defined good Algorithm.

    - Correctness
    - Efficiency
         - Time Complexity -> Running Time
             The benchmark for measuring efficiency in terms of time is 
	      using a worse case scenario is using the last nth trial 
             In this case a range 1-100 search 100th trial to get the target value 100 will be worst case scenario
         - Space Complexity -> Memory Usage

### Algorithm Must have

	- Step:1 An Algorithm must be clear and  have clearly defined problem statement
	
	- Step:2 There must be an input ,There must be an output 
	
	- Step:3 They must contain specific instruction set defined in a particular order of execution
	
	- Step:4 The algorithm must complete and should not take the infinite amount of time {for different same 
	- input scenario} -> this makes the algorithm correct
	
	- Step:5 The Step must be distinct
	
	- Step:6 The execution step should not break into further subtast
	
	- Step:7 The final output an algorithm must be consistent each time it is rerun {for different same input scenario} -> this makes the algorithm 
	
	
### Business Case: Linear Search  
----------------------------------
	Linear Equation time = aX+b 

   - Step1: I am searching for a number 10 in the range of 1-10 

   - Step2: input 1 and 10  to output 10

   - Step3: Steps
      - the numbers has to be sorted
      - Algorithm approach : Linear search in ascending order.
      - Starting with 1, This means that my search will linearly go from 1 until it  get  to the final value 10
     
   <img  height="250" src="https://github.com/erosons/DSA/blob/main/images/hqdefault.jpg" />

	

### Business Case :Binary Search
----------------------------------

The input list of must have been sorted values and the output is position of the final value in the sorted list 
The Binary Search use a binarily divide mechanism and evaluate the target value against the binary value

 ### Scenario Example : target value is 5
	-   A binary search between 1-100, the search starts at 50 and evaluate if 5 > 50 if answer is false:
	-   Search trims off 51-100, and shift to 25 evaluate if 5 > 25 if answer is false
	-   Search trims off 25-50 , and shift to 13 evaluate if 5 > 13 if answer is false
	-   Search trims off 13-25 , and shift to 6 evaluate if 5 > 6 if answer is false
	-   Search trims off 6-13 ,  and shift to 3 evaluate if 5 > 3 if answer is True
	-   Search trims off 1-3 ,  and shift to 5 evaluate if 5 = 5 if answer is True, We have our Final answer compared 

Linear Search - Will have to scan the array to get to target value, It will perform better if the value is 5 , What if the value is
                100, then the Binary search requires just six steps while linear requires 100th steps.


This is measuring magnitude complexity as a function of size O(n)- Upper Bounds, This means measuring algorithm at a worst case scenario

This helps to evaluate algorithm instead of haven't to draw up charts 
Scenario -> (4,10)  (?,10m) If it takes 4 tries when n is 10 , how many trials will it take the algorithm when n is 10 million

For Linear Search -O(n) = Runtime Operation is constant irrespective of the size of the list O(1) =>Constant time
For  Linear Time - O(n)



  
 
    
