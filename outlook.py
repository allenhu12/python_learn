'''
# 自动生成outlook邮件并保存到草稿箱

## 需求

- 定时触发
- 标题包含当前日期和星期几
- 自动填入接收者和抄送者
- 正文包含正确的格式
- 自动保存到草稿箱
'''
import win32com.client
import datetime
from win32com.client import Dispatch, constants

list_weekday = ['星期日', 
                '星期一',
                '星期二',
                '星期三',
                '星期四',
                '星期五',
				'星期六']

const=win32com.client.constants
olMailItem = 0x0
obj = win32com.client.Dispatch("Outlook.Application")
newMail = obj.CreateItem(olMailItem)
# newMail.Subject = "I AM SUBJECT!!"
# newMail.Body = "I AM\nTHE BODY MESSAGE!"
newMail.BodyFormat = 2 # olFormatHTML https://msdn.microsoft.com/en-us/library/office/aa219371(v=office.11).aspx
#newMail.HTMLBody = "<HTML><BODY>Enter the <span style='color:red'>message</span> text here.</BODY></HTML>"
newMail.To = "stanley.zhou@commscope.com"
newMail.CC = "martin.ji@commscope.com"
newMail.Sender = "allen.hu@commscope.com"
#attachment1 = r"C:\Temp\example.pdf"
#newMail.Attachments.Add(Source=attachment1)

now = datetime.datetime.now()
print ("当前系统日期和时间是: ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
dayOfWeek = now.isoweekday() ###返回数字1-7代表周一到周日
print ('today is {0} also means {1}'.format(dayOfWeek,list_weekday[dayOfWeek]))
strDayTime = now.strftime("%Y-%m-%d") + "-" + list_weekday[dayOfWeek]
print (strDayTime)
strMailSubject = 'Weekly Report ' + strDayTime
print(strMailSubject)
newMail.Subject = strMailSubject
strMailBodyStartLine = "Hi, Stanley<br>\
Update the work status to you [{0}]\
".format(now.strftime("%Y-%m-%d"))
newMail.HTMLBody = strMailBodyStartLine + "<HTML><BODY>\
<strong>What did in this week:</strong><ol><li></li><li></li><li></li></ol>\
<strong>Next week plan:</strong><ol><li></li><li></li><li></li></ol>\
<strong>My backlog:</strong><ol><li></li><li></li><li></li></ol>\
</BODY></HTML>"

newMail.display()
newMail.Save()
