
class Driver:
    
    @staticmethod    
    def load_solution(target_function, input_dictionary):
        return target_function(**input_dictionary)
    
    @staticmethod
    def run_test_cases(target_function, input_dictionary, output_list):
        print("Executing Test Cases...")
        for index, test_case in input_dictionary.items():
            test_output = Driver.load_solution(target_function, test_case)
            result_string = "Passed" if test_output == output_list[index] else "Failed"
            print(f"Input: {test_case} | Result = {test_output} -- Output: {output_list[index]} -- {result_string}")    
    
def my_function(num1, num2):
    return num1 + num2

def main():
    input = {
        0: {
            "num1": 1,
            "num2": 2
        },
        1: {
            "num1": 3,
            "num2": 4
        }
    }
    output = [3, 7]
    
    print(Driver.load_solution(my_function, {"num1":1, "num2":2}))
    Driver.run_test_cases(my_function, input, output)
    

if __name__ == '__main__':
    main()
        
    

