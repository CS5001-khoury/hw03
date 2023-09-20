# Homework 3 - Functions

**Divide-Conquer-Glue** whenever we talk about programming, those three terms are at the heart of what we do. Take a problem,
break it into smaller, more abstract parts, conquer those parts, and glue them back together to solve the original problem. That is the heart of programming, and the mindset you need with functions! 

As you work on this assignment, remember the order:

* define
* document
* implement
* test

For every function, you define it, you document it, you implement it, and then you test it - **Before** moving onto the next function!




## Game Helper: Practice at Finding Errors and Writing Tests

Download [game_helper.py](../game_helper.py). It is a file with a series of isolated functions written by another programmer. One thing you will note is there are type hints in the file. This is standard practice in industry, and they are correct! (and won't affect your tests/running). The docstring style used is also standard, and follows the [Google Style Guide](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods) on docstrings. 

👉🏽 **Task** Fix the Syntax Errors in the file. You can run it to find them. 
* For each error, put a line in the game_helper documenting the Syntax error, and how you fixed it. 



👉🏽 **Task** Create a file called **test_game_helper.py**. 
* Include the standard docstring at the top of the file you have seen in all your other assignment files. 
* We have provided a template file [test_game_helper.py](../test_game_helper.py) as an example.
* Write a test for *every* function in game_helper.py, each test should be labeled test_function. For example, a function that tests `area_sq(length: float)`, the function you write should be called `test_area_sq()`. For example:
  * 
  ```python
  def test_area_sq() -> int:
    """Test function for area_sq"""
    print("Testing area_sq")
    fail_count = 0
    if (game_helper.area_sq(5) != 25.0):
        fail_count += 1
        print("....Failed area_sq(5)")
    if (game_helper.area_sq(10.5) != 110.25):
        fail_count += 1
        print("....Failed area_sq(10.5)")
    if (game_helper.fail_count < 1):
        print("....all tests passed for area_sq()")
    return fail_count
    ```
* In each function, you must write **at least two** tests to test each function. The test function will return the number of tests failed, while also printing information about the tests!
* Finally, you should modify main function that calls all the tests, and then prints out the total tests failed. 
  
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

👉🏽 **Task**  Add the output of the run of your test_game_helper.py into your [README.md](../README.md), so TAs can see your output **before** your errors were fixed.

👉🏽 **Task** Fix each logical error until your tests generate 0 errors.   
Feel free to make comments about logical errors and this process after this is done

> Further Thinking, in an ideal world you would be writing each test after each function was written or in test driven development including agile development writing the test *before* the function is written!

## Color Blindness Tester
Roughly 8% of Northern European Descent are colorblind. However, application developers often fail to develop applications that can been seen by individuals with colorblindness, or even worse, they use colors to convey information that is not available in any other way. A recent example had a bus route applications that put 
blue on green to indicate a bus was on time. This was not accessible to individuals with colorblindness.

In this assignment, you will write a program that will test if a color is visible to individuals with colorblindness. 

### Understanding Color Blindness

There are many different types of color blindness. The most common is red-green color blindness. This is where the individual has trouble distinguishing between red and green. For this assignment, we will be filtering
colors based on three types of color blindness: Protanopia, Deuteranopia, and Tritanopia.

* Protanopia - Red and Green is reduced in intensity.
* Deuteranopia - Green is reduced in intensity.
* Tritanopia - Blue is reduced in intensity.

While this assignment over simplifies the testing of these colors (spoiler: this could be a fun final project to improve upon), it will give you a sense of how to use functions to break down a problem into smaller parts.

### Understanding RGB Values

RGB stands for Red, Green, Blue. It is a way of representing colors in a computer. Each color is represented by a number between 0 and 255. For example, the color white is represented by (255, 255, 255) and the color black is represented by (0, 0, 0). For this assignment we will be using RGB values. While true color is often a much wider range, and can include alpha (transparency) values, we will be using the simplified version.

While the code is provided, you will also print out the HTML values for the colors. HTML colors are represented by a # followed by 6 hexadecimal digits. For example, white is #FFFFFF and black is #000000. A hexadecimal digit is a number between 0 and 9, or a letter between A and F. The letters A through F represent the numbers 10 through 15. For example, the number 10 in hexadecimal is A, and the number 15 in hexadecimal is F. As you are covering binary in CS 5002 which is a "base 2" notation of numbers, hexadecimal is a "base 16" notation of numbers compared to our standard "base 10" notation. The reason HTML uses hexadecimal is because it is a more compact way of representing colors, representing 3 bytes (0-255) of information in 6 digits.


### Implementation and Testing
You will find [ColorTesterDesign](ColorTesterDesign.md) in this folder. It is a design document that will help you break down the problem into smaller parts. You will want to read through this document, and then slowly practice

* defining
* documenting
* implementing
* testing

for every function you are required to implement! Make sure to take it into small parts, and run and test your code regularly.  The over arching concept behind the project is your manager has given you this design document to work on and your job as a junior developer is to implement their design. In practice you are given more freedom as a developer, but this is a good way to practice breaking down a problem into smaller parts. 

As you work on the project, take a look at some of the resources below. Sometimes seeing the actual colors it is generating is helpful to understanding the problem.

👉🏽 **Task**  - Implement [color_tester.py](../color_tester.py) and [test_color_tester.py](../test_color_tester.py) using the information provided by [ColorTesterDesign](ColorTesterDesign.md)

## README.md
As per usual, make sure you answer the questions in the [README.md](../README.md) file. They will require
further research, especially on your opinions about universal/inclusive design of applications. 

### Inclusive Design Resources
* [Microsoft Inclusive Design](https://inclusive.microsoft.design/)
* [What is Inclusive Design](http://www.inclusivedesigntoolkit.com/whatis/whatis.html)
* [W3Schools Design Tips](https://www.w3.org/WAI/tips/designing/)
* [10 Essential Guidelines for Colorblind Friendly Design](https://www.colorblindguide.com/post/colorblind-friendly-design-3)
* [Color Blindness Simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/)

## Grading Rubric

### Files
Your final submission will consist of the following files:
* game_helper.py
* test_game_helper.py
* color_test.py
* test_color_tester.py
* README.md


### Rubric
1. Learning (AG)
   * game_helper properly corrected and passes tests
   * test_game_helper has the required functions
2. Approaching  (AG)
   * color_tester.py properly implemented color_difference, and blindness filters
   * test_color_tester.py has the required functions
   * get_number_from_client works in basic cases between 0 and 255
   * run_checks returns proper value, and prints properly
3. Meets  (AG)
   * get_number_from_client properly handles invalid input not in 0 <= n <= 255
     * also prints error message properly 
   * game_helper, test_game_helper and color_tester pass python style checker
4. Exceeds  (MG)
   * test_game_helper.py has at least two tests for every function in game_helper.py
   * output is accurately reported in README.md
   * test_color_tester.py has testing function for every function in color_tester.py (excluding main, and print_html_values, and provided functions)
   * All .py files include proper docstrings - both file header and function level
   * README.md questions answered correctly, showing research and deeper knowledge


AG - Auto-graded  
MG - Manually graded

### Submission Reminder 🚨
For manually graded elements, we only guarantee time to submit for a regrade IF you submit by the DUE DATE. Submitting late may mean it isn't possible for the MG to be graded before the AVAILABLE BY DATE, removing any windows for your to resubmit in time. While it will be graded, it is always best to submit by the due date, so you have full opportunity to improve your grade.

## 📚 Additional Resources

In game_helper.py we make use of **type hints**. These were introduced in Python 3.0, but they weren't really given a purpose until Python 3.5 (PEP 484). It has become common in industry to include them even though python is a dynamically typed language. Dynamically typed means specifying the types are not required as the language will determine the memory needed at runtime. Some languages, like Java which you will learn in CS5004, are strongly typed which means the types are required and strictly enforced at time of programming (compile time). 

Adding the type hints in python is two fold. First, it makes it easier to see what is expected both as the arguments of a function and as the return value of the function. This helps you debug and helps other programmers. Second, there are tools that someone can run against your code to make sure the types are being followed, such as mypy below! This matters for large scale application development.

While not required for this course, you can learn about types hints
* [mypy](https://mypy.readthedocs.io/en/latest/)
* [typing library](https://docs.python.org/3/library/typing.html)

Above all, keep it simple! There are far more features in python than we will need. 

Eventually when we move to an IDE other than IDLE, type hints will also make documentation generation easier.
