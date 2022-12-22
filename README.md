# Homework 3 - Functions

**Divide-Conquer-Glue** whenever we talk about programming, those three terms are at the heart of what we do. Take a problem,
break it into smaller, more abstract parts, conquer those parts, and glue them back together to solve the original problem. That is the heart of programming, and the mindset you need with functions! 

As you work on this assignment, remember the order:

* define
* document
* implement
* test

For every function, you define it, you document it, you implement it, and then you test it - **Before** moving onto the next function!

> Please note, for this assignment you will be adding to your README.md as you work. You will actually want to create that first!
> We will highlight questions to answer in the README.md as you are working!
>
> To make grading easier, we ask that you use the following template for your README.md
> ````text
> # Homework 3: Readme
> 
> * Semester: UPDATE
> * Student: Your name
> 
> ## game_helper error tracking
> * syntax error one
> * syntax error two..
> * etc
>
> ```text
> output of your test_game_helper.py run
> ```
> Comments about Logical errors and questions
>
> 
> ## Reflection and Further Thinking
>
>````
> This format will help make is easier for the grader to quickly find the sections of your file. As a reminder, you can use 
> any text editor for your markdown file, just make sure to save the extension as .md



## Game Helper Tests

Download [game_helper.py](game_helper.py). It is a file with a series of isolated functions written by another programmer. One thing you will note is there are type hints in the file. This is standard practice in industry, and they are correct! (and won't affect your tests/running). The docstring style used is also standard, and follows the [Google Style Guide](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods) on docstrings. 

👉🏽 **Task** Fix the Syntax Errors in the file. You can run it to find them. 
* For each error, put a line in the game_helper documenting the Syntax error, and how you fixed it. 



👉🏽 **Task** Create a file called **test_game_helper.py**. 
* Include the standard docstring at the top of the file you have seen in all your other assignment files. 
* Write a test for *every* function in game_helper.py, each test should be labeled test_function. For example, a function that tests `area_sq(length: float)`, the function you write should be called `test_area_sq()`.
* To help with the auto-grader, please use the following import line  
```python
from .game_helper import area_sq, area_rec, vol_cube, area_triangle, can_add, roll_dice, vol_pyramid
```
* while the above line is not standard, it will help with path conflict issues with the auto-grader.
* In each function, you must write **at least two** tests to test each function. The test function will return the number of tests failed, while also printing information about the tests!
* Finally, you should add a main function that calls all the tests, and then prints out the total tests failed. 

Here is an example run using our test_game_helper.py.

```text
Running all tests
Testing area_sq
....Failed area_sq(5)
....Failed area_sq(10.5)
Testing area_rec
....all tests passed for area_rec()
Testing vol_cube
....Failed vol_cube(10, 12, 10)
....Failed vol_cube(0.2, 10, 5.3)
Testing area_triangle
....Failed area_triangle(10, 10)
....Failed area_triangle(4.2, 17)
Testing vol_pyramid
....Failed vol_pyramid(5, 15)
Testing can_add
....Failed can_add(10, 10, 20)
Testing roll_dice
....Failed roll_dice()
....Failed roll_dice(13)
Failed 10 tests.
```
(btw using the ```text block is how that block was generated in this readme)

👉🏽 **Task**  Add the output of the run into your README.md, so TAs can see your output before your errors were fixed.

👉🏽 **Task** Fix each logical error until your tests generate 0 errors. 
* Feel free to make comments about logical errors and this process after this is done

> Further Thinking, in an ideal world you would be writing each test after each function was written or in test driven development including agile development writing the test *before* the function is written!

## Star Rating App


Highlight each major component with a section, add **task** for tasks and include 👉🏽 or something obvious so they can be found easily. 

## Grading Rubric


Add (AG) and (MG) next to tiers, add major conditions to meet to pass each tier. 

1. Learning ()
   * 
2. Approaching  ()
   * 
3. Meets  ()
   * 
4. Exceeds  ()
   * 


AG - Auto-graded  
MG - Manually graded


## Additional Resources (optional)
Use this section to keep the homework description shorter, and instead talk about additional resources down here (such as tools to use, websites to review, etc)
