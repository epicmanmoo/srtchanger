def is_int_string(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def read_file(file):
    movie_content = []
    ext_en = file.split(".")
    f_n = ext_en[0]
    movie_content.append(f_n)
    if ext_en[1] != "srt":
        print("Not a valid .srt file")
        return
    else:
        m_file = open(file, "r")
        content = m_file.readlines()
        second_last = m_file.readline()
        last_line = m_file.readline()
        for line in content:
            if (":" in line and "," in line and "-->" in line) or is_int_string(line):
                movie_content.append(line)
                second_last = last_line
                last_line = line
        m_file.close()
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
                if f_value < 1 and int(f_value) == 0:
                    spl_ms = value.split(".")
                    if "-" in spl_ms[0]:
                        ms_v = int(spl_ms[1]) * -1
                    else:
                        ms_v = int(spl_ms[1])
                    if ms_v > 999:
                        return
                    ms_start += ms_v
                    ms_finish += ms_v
                    if ms_start > 999:
                        ms_start = ms_start - 1000
                        sec_start += 1
                        if sec_start > 59:
                            sec_start = 0
                            min_start += 1
                            if min_start > 59:
                                min_start = 0
                                hours_start = 1
                    if ms_finish > 999:
                        ms_finish = ms_finish - 1000
                        sec_finish += 1
                        if sec_finish > 59:
                            sec_finish = 0
                            min_finish += 1
                            if min_finish > 59:
                                min_finish = 0
                                hours_finish = 1
                    if ms_start < 0:
                        ms_start = ms_start + 1000
                        sec_start -= 1
                        if sec_start < 0:
                            sec_start = 59
                            min_start -= 1
                            if min_start < 0:
                                min_finish = 59
                                hours_finish = 0
                    if ms_finish < 0:
                        ms_finish = ms_finish + 1000
                        sec_finish -= 1
                        if sec_finish < 0:
                            sec_finish = 59
                            min_finish -= 1
                            if min_finish < 0:
                                min_finish = 59
                                hours_finish = 0
                else:
                    spl_s = value.split(".")
                    s_v = int(spl_s[0])
                    ms_v = int(spl_s[1])
                    if s_v < 0 or s_v > 59 or ms_v > 999 or ms_v < 0:
                        return
                    sec_start += s_v
                    ms_start += ms_v
                    sec_finish += s_v
                    ms_finish += ms_v
                    if sec_start > 59:
                        sec_start = sec_start - 60
                        min_start += 1
                        if min_start > 59:
                            min_start = 0
                            hours_start += 1
                    if sec_finish > 59:
                        sec_finish = sec_finish - 60
                        min_finish += 1
                        if min_finish > 59:
                            min_finish = 0
                            hours_finish += 1
                    if sec_start < 0:
                        sec_start = sec_start + 60
                        min_start -= 1
                        if min_start < 0:
                            min_start = 59
                            hours_start -= 1
                    if sec_finish < 0:
                        sec_finish = sec_finish + 60
                        min_finish -= 1
                        if min_finish < 0:
                            min_finish = 59
                            hours_finish -= 1
                    if ms_start > 999:
                        ms_start = ms_start - 1000
                        sec_start += 1
                        if sec_start > 59:
                            sec_start = 0
                            min_start += 1
                            if min_start > 59:
                                min_start = 0
                                hours_start = 1
                    if ms_finish > 999:
                        ms_finish = ms_finish - 1000
                        sec_finish += 1
                        if sec_finish > 59:
                            sec_finish = 0
                            min_finish += 1
                            if min_finish > 59:
                                min_finish = 0
                                hours_finish = 1
                    if ms_start < 0:
                        ms_start = ms_start + 1000
                        sec_start -= 1
                        if sec_start < 0:
                            sec_start = 59
                            min_start -= 1
                            if min_start < 0:
                                min_finish = 59
                                hours_finish = 0
                    if ms_finish < 0:
                        ms_finish = ms_finish + 1000
                        sec_finish -= 1
                        if sec_finish < 0:
                            sec_finish = 59
                            min_finish -= 1
                            if min_finish < 0:
                                min_finish = 59
                                hours_finish = 0
                if sec_start < 10:
                    sec_start = '0' + str(sec_start)
                if sec_finish < 10:
                    sec_finish = '0' + str(sec_finish)
                if ms_start < 10:
                    ms_start = '00' + str(ms_start)
                elif 100 > ms_start > 10:
                    ms_start = '0' + str(ms_start)
                if ms_finish < 10:
                    ms_finish = '00' + str(ms_finish)
                elif 100 > ms_finish > 10:
                    ms_finish = '0' + str(ms_finish)
                if ms_start == 10:
                    ms_start = '100'
                if ms_finish == 10:
                    ms_finish = '100'
                hours_start = str(hours_start)
                hours_finish = str(hours_finish)
                if hours_start == "0.0" or hours_start == '0':
                    hours_start = "00"
                if hours_finish == "0.0" or hours_finish == '0':
                    hours_finish = "00"
                if hours_start == "1.0" or hours_start == '1':
                    hours_start = "01"
                if hours_finish == "1.0" or hours_finish == '1':
                    hours_finish = "01"
                if len(str(min_start)) == 1:
                    min_start = str('0' + str(min_start))
                if len(str(min_finish)) == 1:
                    min_finish = str('0' + str(min_finish))
                this_row_start_str = hours_start + ":" + str(min_start) + ":" + str(sec_start) + "," + \
                    str(ms_start) + " --> " + hours_finish + ":" + str(min_finish) + ":" + str(sec_finish) + "," + \
                    str(ms_finish)
                changed_content.append(this_row_start_str)
            except IndexError:
                continue
    return changed_content


def change_file(file, n_file, content):
    the_file = open(file, "r")
    new_file = open(n_file, "w")
    row_index = 0
    for line in the_file.readlines():
        if ":" in line and "," in line and "-->" in line:
            new_file.write(content[row_index] + '\n')
            row_index += 1
        else:
            new_file.write(line)
    the_file.close()
    new_file.close()


def check_file(n_file):
    the_file = open(n_file, "r")
    content = the_file.readlines()
    for line in content:
        if ":" in line and "," in line and "-->" in line:
            if len(line) != 30:
                print("ERROR:", line)


file1 = "hostel2.srt"
file2 = "hostel2ch.srt"
before = read_file(file1)
movie_name = before[0].upper()
num_of_lines = before[len(before) - 1].strip()
del before[0]
del before[len(before) - 1]
print(movie_name + ' with ' + num_of_lines + ' lines')
in_value = "6.000"
after = change_to(before, in_value)
try:
    change_file(file1, file2, after)
except Exception:
    pass
check_file(file2)
