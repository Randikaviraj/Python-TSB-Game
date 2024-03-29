from little_battle import load_config_file
# Don't remove any comments in this file
folder_path = "./invalid_files/"

# Please create appropriate invalid files in the folder "invalid_files"
# for each unit test according to the comments below and
# then complete them according to the function name

def test_file_not_found():
  # no need to create a file for FileNotFound
  if assertionChecker(load_config_file,folder_path+"unkownfile",FileNotFoundError):
    print("Test Passed")
  else:
    print("Test Failed")

def test_format_error():
  # add "format_error_file.txt" in "invalid_files"
  if assertionChecker(load_config_file,folder_path+"format_error_file.txt",SyntaxError):
    print("Test Passed")
  else:
    print("Test Failed")
    
def test_frame_format_error():
  # add "frame_format_error_file.txt" in "invalid_files"
  if assertionChecker(load_config_file,folder_path+"frame_format_error_file.txt",SyntaxError):
    print("Test Passed")
  else:
    print("Test Failed")

def test_frame_out_of_range():
  # add "format_out_of_range_file.txt" in "invalid_files"
  if assertionChecker(load_config_file,folder_path+"format_out_of_range_file.txt",ArithmeticError):
    print("Test Passed")
  else:
    print("Test Failed")
def test_non_integer():
  # add "non_integer_file.txt" in "invalid_files"
  if assertionChecker(load_config_file,folder_path+"non_integer_file.txt",ValueError):
    print("Test Passed")
  else:
    print("Test Failed")

def test_out_of_map():
  # add "out_of_map_file.txt" in "invalid_files"
  if assertionChecker(load_config_file,folder_path+"out_of_map_file.txt",ArithmeticError):
    print("Test Passed")
  else:
    print("Test Failed")

def test_occupy_home_or_next_to_home():
  # add two invalid files: "occupy_home_file.txt" and
  # "occupy_next_to_home_file.txt" in "invalid_files"
  if assertionChecker(load_config_file,folder_path+"occupy_home_file.txt",ValueError):
    print("Test Passed")
  else:
    print("Test Failed")
  if assertionChecker(load_config_file,folder_path+"occupy_next_to_home_file.txt",ValueError):
    print("Test Passed")
  else:
    print("Test Failed")

def test_duplicate_position():
  # add two files: "dupli_pos_in_single_line.txt" and
  # "dupli_pos_in_multiple_lines.txt" in "invalid_files"
  if assertionChecker(load_config_file,folder_path+"dupli_pos_in_single_line.txt",SyntaxError):
    print("Test Passed")
  else:
    print("Test Failed")
    
def test_odd_length():
  # add "odd_length_file.txt" in "invalid_files"
  if assertionChecker(load_config_file,folder_path+"odd_length_file.txt",SyntaxError):
    print("Test Passed")
  else:
    print("Test Failed")

def test_valid_file():
  if not(assertionChecker(load_config_file,"config.txt",Exception)):
    print("Test Passed")
  else:
    print("Test Failed")

def assertionChecker(func,filepath,exception):
  try:
    func(filepath)
  except exception as e:
    print("=======================================================================================")
    print("Error Raised :"+str(e))
    print("=======================================================================================")
    return True
  except:
    return False
  return False

# you can run this test file to check tests and load_config_file
if __name__ == "__main__":
  test_file_not_found()
  test_format_error()
  test_frame_format_error()
  test_frame_out_of_range()
  test_non_integer()
  test_out_of_map()
  test_occupy_home_or_next_to_home()
  test_duplicate_position()
  test_odd_length()
  test_valid_file()