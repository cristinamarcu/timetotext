from convert import convert_time_to_text, get_current_time
import sys

if len(sys.argv) > 1:
    print(convert_time_to_text(sys.argv[1]))
else:
    time_now = get_current_time()
    print(convert_time_to_text(time_now))
