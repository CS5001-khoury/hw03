"""
    Student:
    Semester:

    Helps with testing color_tester.py
"""

import color_tester

def test_delta() -> int:
    """Tests the delta function. 
    
    Returns the number of tests that failed.
    """
    # 255, 255, 255, 0, 0, 0 - should give a difference of 1
    failed = 0
    if color_tester.delta(255, 255, 255, 0, 0, 0) != 1:
        print("Failed delta test with (255, 255, 255) and (0, 0, 0)") 
        failed += 1
    # 255, 255, 255, 255, 255, 255 - should give a difference of 0
    if color_tester.delta(255, 255, 255, 255, 255, 255) != 0:
        print("Failed delta test with (255, 255, 255) and (255, 255, 255)") 
        failed += 1
    # 255, 255, 255, 127, 127, 127 - should give a difference of 0.5
    delta = round(color_tester.delta(255, 255, 255, 127, 127, 127), 2) #rounding because of floating point errors
    if  delta != 0.5:
        print(f"Failed delta test with (255, 255, 255) and (127, 127, 127), delta = {delta}") #this way we can see what it was 
        failed += 1
    return failed    
    




def run_all() -> None:
    """Runs all tests, continue to update this with functions as you add them"""
    fail_count = 0
    fail_count += test_delta()
    ## add more here as you add more functions, notice the += above adding teh return value to the fail_count


    ## and then giving feedback
    print(f"Failed {fail_count} tests")

if __name__ == '__main__':
    run_all() 