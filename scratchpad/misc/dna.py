from typing import Any, Callable

class DNATools:
    BASE_PAIR_COMPLEMENTS: dict[str, str] = {
        'A' : 'T',
        'T' : 'A',
        'C' : 'G',
        'G' : 'C'
    }
    
    @classmethod
    def reverse_strand(cls, sequence: str) -> str:
        return sequence[::-1]
    
    @classmethod
    def get_complement(cls, sequence: str) -> str:
        return ''.join(cls.BASE_PAIR_COMPLEMENTS[base_pair] for base_pair in sequence)
    
    @classmethod
    def compress(cls, sequence: str) -> str:
        def append_to_list(count: int, base_pair: str, result_list: list[str]):
            numeric_prefix = "" if count <= 1 else str(count)
            result_list.append(numeric_prefix + base_pair)
            
        if len(sequence) <= 1:
            return sequence
               
        result_list: list[str] = []
        last_base_pair: str = sequence[0]
        count: int = 1
        
        for base_pair in sequence[1:]:
            if base_pair == last_base_pair:
                count += 1
            else:
                append_to_list(
                    count=count, 
                    base_pair=last_base_pair, 
                    result_list=result_list
                    )
                count = 1
            last_base_pair = base_pair
            
        # Need to append last character to list
        append_to_list(
                    count=count, 
                    base_pair=last_base_pair, 
                    result_list=result_list
                    )
        
        return ''.join(result_list)
    
    @classmethod
    def expand(self, sequence: str):
        result: str = ''
        
        count = 0
        for character in sequence:
            if character.isdigit():
                count = int(character)
            else:
                if count > 1:
                    uncompressed_string: str = count * character 
                    result += uncompressed_string
                    count = 0
                else:
                    result += character
        
        return result

class TestData:
    def __init__(self, 
                 test_function: Callable[[str], str], 
                 test_input: str, 
                 expected_result: str):
        self.function: Callable[[str], str] = test_function
        self.input: str = test_input
        self.result: str = expected_result
        
    def get_attributes(self):
        return (self.function, self.input, self.result)

def display_test_result(expected_result: str, actual_result: str) -> None:
    result: str = "PASSED"
    
    try:
        assert expected_result == actual_result
    except AssertionError:
        result = "FAILED"
        
    print(f"Test {result}: Expected '{expected_result}' and observed '{actual_result}'.")

def run_test(function: Callable[[str], str], test_input:str, expected_result: str) -> None:
    actual_result = function(test_input)
    display_test_result(
        expected_result=expected_result,
        actual_result=actual_result
    )

def main() -> None:
    
    testcases: list[TestData] = [
        TestData(
            test_function = DNATools.reverse_strand,
            test_input = 'AATCG',
            expected_result= 'GCTAA'
        ),
        TestData(
            test_function = DNATools.get_complement,
            test_input = 'ATCGG',
            expected_result= 'TAGCC'
        ),
        TestData(
            test_function = DNATools.compress,
            test_input = 'CCAAAT',
            expected_result= '2C3AT'
        ),
        TestData(
            test_function = DNATools.expand,
            test_input = 'CA2G3T',
            expected_result= 'CAGGTTT'
        )
    ]
    
    for function, input, result in [test.get_attributes() for test in testcases]:
        print(f"Testing: {function.__name__} (Input: {input})")
        run_test(
            function=function,
            test_input=input,
            expected_result=result
        )
        print("")
    
if __name__ == '__main__':
    main()