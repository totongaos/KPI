def def_checkOut(count_staff): #hàm check out
 print(f"You have Done: {count_staff}. You have not done out: {KPI - count_staff}")
def def_checkIn(count_staff):  #hàm check in
 print(f"You must reach a KPI of {KPI}. You have not done in: {KPI - count_staff}")


KPI = 3
count_staff = 0
count_phieu = 0
lst_staff = []
lst_phieu = []
dict_phieu = {}
check_in = "F"

while count_staff < 3:
 # check_in = input("If u check in, please u enter T: ")
 print('a')
 if check_in == "T":
  id_staff = input("Please enter your id: ")
  lst_staff.count(id_staff)
  count_staff = lst_staff.count(id_staff)
  check_out = "F"
  if count_phieu == KPI:
   print("You reach KPI!")
   check_out == "T"
   check_in == "F"

  def_checkIn(count_staff)
  print("- " * 20)


  while check_out == "F":
   name_phieu = input("Please enter your name_phieu: ")

   dict_phieu.update({name_phieu : id_staff})
   lst_staff.append(id_staff)
   # lst_phieu.append(dict_phieu.keys())
   # lst_phieu.append(name_phieu)
   count_staff = lst_staff.count(id_staff)
   # count_phieu = lst_phieu.count(name_phieu)
   if count_staff == KPI:
    print("You reach KPI!")
    check_out == "T"
    break

   check_out = input("If u no check out, please u enter F: ")

   if check_out != "F":
    def_checkOut(count_staff)
    print("- " * 20)

  count_staff = lst_staff.count(id_staff)
  # count_phieu = lst_phieu.count(name_phieu)

  print(dict_phieu)

  print('count_staff',count_staff,'lst_staff',lst_staff)
  # print('count_phieu',count_phieu,'lst_phieu',lst_phieu)

 else:
  print('b')
  check_in = input("If u check in, please u enter T: ")

