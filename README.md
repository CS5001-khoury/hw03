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

For this part of the homework, make sure to complete the [Design Activity](https://github.com/CS5001-khoury/Handouts/raw/main/Module3/design_star_rating_app.docx) first. You will turn in a PDF of the design activity, and make sure to include all the names of the people who worked with you on it (since it can be done with others). 

Based on the activity, you will want to use the [star_rating_app.py](star_rating_app.py) as a template file. The function names matter so we can unit test and grade - so please use the template. You can add functions, but do not take away any of the provided functions as we will be using them in our tests. 


👉🏽 **Task** Complete the Star Rating App, and submit both star_rating_app.py and test_star_rating_app.py. Note that testing client input and output can be difficult, as the tests are interactive. That is fine. You can add comments talking about how you did the interactive test. However, the important part is to make sure you test your work before submitting. 


## Reflection

👉🏽 **Task** In your README.md add a small paragraph reflection of your learning and progress. Remember, this is not just a list of items, but we encourage you to critically evaluate and think about your learning process. There is a lot of research as to the benefits of reflection and retention of information - especially related to computer science!

## Grading Rubric

### Files
Your final submission will consist of the following files:
* game_helper.py
* test_game_helper.py
* star_rating_app.py
* test_star_rating_app.py
* design_star_rating.pdf 
* README.md


### Rubric
1. Learning (AG)
   * game_helper properly corrected and passes tests
   * test_game_helper has the required functions
2. Approaching  (AG)
   * star_rating_app works with simple entries and ratings
3. Meets  (AG)
   * test_game_helper catches errors on another version of game_helper 
     * Same functions but  may hold different logical errors
   * star_rating_app works with more complex entry
     * case change on add,list,exit or doesn't break when using wrong words
     * properly using constants throughout code
   * Both game_helper and star_rating pass python style checker
4. Exceeds  (MG)
   * test_game_helper.py has at least two tests for every function in game_helper.py
   * output is accurately reported in README.md
   * test_star_rating_app has reasonable tests in it
   * All .py files include proper docstrings - both file header and function level
   * design_star_rating.pdf has been completed properly 
     * If you worked as a group on it, you all need to submit even if the document is the same, and include everyone's name on the document
   * README.md defines syntax errors fixed
   * README.md includes at least a paragraph reflection.


AG - Auto-graded  
MG - Manually graded


## Additional Resources (optional)

In game_helper.py we make use of **type hints**. These were introduced in Python 3.0, but they weren't really given a purpose until Python 3.5 (PEP 484). It has become common in industry to include them even though python is a dynamically typed language. Dynamically typed means specifying the types are not required as the language will determine the memory needed at runtime. Some languages, like Java which you will learn in CS5004, are strongly typed which means the types are required and strictly enforced at time of programming (compile time). 

Adding the type hints in python is two fold. First, it makes it easier to see what is expected both as the arguments of a function and as the return value of the function. This helps you debug and helps other programmers. Second, there are tools that someone can run against your code to make sure the types are being followed, such as mypy below! This matters for large scale application development.

While not required for this course, you can learn about types hints
* [mypy](https://mypy.readthedocs.io/en/latest/)
* [typing library](https://docs.python.org/3/library/typing.html)

Above all, keep it simple! There are far more features in python than we will need. 

Eventually when we move to an IDE other than IDLE, type hints will also make documentation generation easier.
