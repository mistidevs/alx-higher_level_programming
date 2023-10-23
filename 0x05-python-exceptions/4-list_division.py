#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length

    for i in range(list_length):
        try:
            new_list[i] = my_list_1[i] / my_list_2[i]
        except (TypeError, ZeroDivisionError) as e:
            if isinstance(e, TypeError):
                print("wrong type")
            elif isinstance(e, ZeroDivisionError):
                print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            pass
    return new_list

if __name__ == '__main__':
    list_division()
