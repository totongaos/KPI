def noty_checkOut(count_staff): #hàm noty check out
 print(f"You have Done: {count_staff}. You have not done out: {KPI - count_staff}")
 print('- '*20)
def noty_checkIn(count_staff):  #hàm noty check in
 print(f"You must reach a KPI of {KPI}. You have not done in: {KPI - count_staff}")
 print('- '*20)


KPI = 4
count_staff = 0
lst_staff = []

count_ticket = 0
lst_ticket = []

dict_ticket = {}
check_in = "F"

while count_staff < KPI:
 if check_in == "T":
  if count_ticket == KPI: #check đủ KPI chưa
   print("***You reach KPI! ***")
   check_out == "T"
   check_in == "F"
  else: # nếu chưa đạt KPI
   id_staff = input("Please enter your id: ")
   count_staff = lst_staff.count(id_staff) # để đếm lại số lượng id staff ứng với ud vào
   check_out = "F" # cho check out = Flase

   noty_checkIn(count_staff) # chạy hàm noty checkIn

  while check_out == "F":
   name_ticket = input("Please enter your name_ticket: ")  # nhập tên phiếu
   if name_ticket not in lst_ticket:  # nếu tên phiếu không trong list phiếu
    dict_ticket.update({name_ticket: id_staff})  # thêm tên phiếu và id staff vào dict
    lst_staff.append(id_staff)  # thêm id_staff vào list
    lst_ticket.append(name_ticket)  # thêm tên phiếu vào list
   else:  # nếu tên phiếu trong list phiếu -> báo lỗi
    print("This ticket has already been completed. Please enter another ticket")

   count_staff = lst_staff.count(id_staff)  # đếm số lượng id staff trong list để noty
   if count_staff == KPI:  # check đủ KPI chưa sau khi đếm. fix bug sau khi nhập đủ r, nhưng vãn hỏi staff có checl out ko
    print("*** You reach KPI! ***")
    check_out == "T"
    break
   check_out = input("If u no check out, please u enter F: ") #hỏi staff đã muốn về hay chưa
   if check_out != "F": #nếu staff về thì noty về
    noty_checkOut(count_staff)

  count_staff = lst_staff.count(id_staff) # đếm lại số lượng id staff trong list để noty check in
  print(dict_ticket) #print để check dict
  print('count_staff',count_staff,'lst_staff',lst_staff) #print để check noty

 else: #nếu ko check in thì hỏi lại
  check_in = input("If u check in, please u enter T: ")

