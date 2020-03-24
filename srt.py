import decimal
import os


def is_int_string(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def read_file():
    movie_content = []
    second_last = None
    last_line = None
    file_name = "hostel2.srt"
    ext_en = os.path.splitext(file_name)
    movie_content.append(ext_en[0])
    ext_en = ext_en[1]
    if ext_en != ".srt":
        print("Not a valid .srt file")
    else:
        file = open("hostel2.srt", "r")
        content = file.readlines()
        second_last = file.readline()
        last_line = file.readline()
        for line in content:
            if (":" in line and "," in line and "-->" in line) or is_int_string(line):
                movie_content.append(line)
                second_last = last_line
                last_line = line
        file.close()
        movie_content.append(second_last)
        return movie_content


def change_to(the_file, value):
    changed_content = []
    for line in the_file:
        if ":" in line and "," in line and "-->" in line:
            try:
                spl_val = value.split(".")
                if len(spl_val[1]) != 3:
                    return
                if len(value) < 5:
                    return
                this_line = line
                start_finish = this_line.split("-->")
                start = start_finish[0]
                finish = start_finish[1]
                split_start = start.split(":")
                split_finish = finish.split(":")
                s_ms_start = split_start[2].split(",")
                s_ms_finish = split_finish[2].split(",")
                hours_start = float(split_start[0])
                min_start = int(split_start[1])
                sec_start = int(s_ms_start[0])
                ms_start = int(s_ms_start[1])
                hours_finish = float(split_finish[0].strip())
                min_finish = int(split_finish[1])
                sec_finish = int(s_ms_finish[0])
                ms_finish = int(s_ms_finish[1])
                f_value = float(value)
                if f_value < 1:
                    spl_ms = value.split(".")
                    ms_v = int(spl_ms[1])
                    ms_start += ms_v
                    ms_finish += ms_v
                    if ms_start > 999:
                        sec_start += 1
                        ms_start = ms_start - 1000
                    if ms_finish > 999:
                        sec_finish += 1
                        ms_finish = ms_finish - 1000
                else:
                    pass
                hours_start = str(hours_start)
                hours_finish = str(hours_finish)
                if hours_start == "0.0":
                    hours_start = "00"
                if hours_start == "1.0":
                    hours_start = "01"
                if hours_finish == "0.0":
                    hours_finish = "00"
                if hours_finish == "1.0":
                    hours_finish = "01"
                if len(str(min_start)) == 1:
                    min_start = str('0' + str(min_start))
                if len(str(min_finish)) == 1:
                    min_finish = str('0' + str(min_finish))
                if len(str(sec_start)) > 2:
                    sec_start = str(sec_start)
                    sec_start = sec_start[0:2]
                if len(str(sec_finish)) > 2:
                    sec_finish = str(sec_finish)
                    sec_finish = sec_finish[0:2]
                if len(str(ms_start)) == 1:
                    ms_start = str(ms_start) + "00"
                if len(str(ms_start)) == 2:
                    ms_start = str(ms_start) + "0"
                if len(str(ms_finish)) == 1:
                    ms_finish = str(ms_finish) + "00"
                if len(str(ms_finish)) == 2:
                    ms_finish = str(ms_finish) + "0"
                if len(str(ms_start)) == 4:
                    ms_start = str(ms_start)[0:2] + "0"
                if len(str(ms_finish)) == 4:
                    ms_finish = str(ms_finish)[0:2] + "0"
                if len(str(ms_start)) == 5:
                    ms_start = str(ms_start)[0:3]
                if len(str(ms_finish)) == 5:
                    ms_finish = str(ms_finish)[0:3]
                this_row_start_str = hours_start + ":" + str(min_start) + ":" + str(sec_start) + "," + str(ms_start) + " --> " + hours_finish + ":" + str(min_finish) + ":" + str(sec_finish) + "," + str(ms_finish)
                changed_content.append(this_row_start_str)
            except IndexError:
                continue
    return changed_content


def change_file(content):
    the_file = open("hostel2.srt", "r")
    new_file = open("hostel2ch.srt", "w")
    row_index = 0
    for line in the_file.readlines():
        if ":" in line and "," in line and "-->" in line:
            new_file.write(content[row_index] + '\n')
            row_index += 1
        else:
            new_file.write(line)
    the_file.close()
    new_file.close()


before = read_file()
movie_name = before[0].upper()
num_of_lines = before[len(before) - 1].strip()
del before[0]
del before[len(before) - 1]
# print(movie_name + ' with ' + num_of_lines + ' lines')
after = change_to(before, "0.900")
try:
    change_file(after)
except Exception:
    pass

