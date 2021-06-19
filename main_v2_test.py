from PgEngine import *
from _data_config import *


if __name__ == "__main__":
    login = loginger()
    dc,basic_dict = login.run()
    person = dc.give_me_a_person_with_data()
    