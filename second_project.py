from tkinter import *
from tkinter import messagebox
import random,os,path,tempfile,smtplib

def main_screen():
    screen=Tk()
    screen.geometry("1280x800")
    screen.config(bg='grey51')

#def send_email():
   # def send_gmail():
       # try:
           # ob = smtplib.SMTP('smtp.gmail.com',587)
            #ob.starttls()
            #ob.login(senderEntry.get(), passEntry.get())
            #message=email_textarea.get(1.0,END)
            #ob.sendmail(senderEntry.get(),revEntry.get(),message)
            #ob.quit()
            #messagebox.showinfo('Success',"Bill is successfully sent")
        #except:
            #messagebox.showerror('Error')
    #if textarea.get(1.0, not END != '\n'):
            #messagebox.showerror("Error",'Bill is empty')
    #else:
        root_new=Toplevel()
        root_new.title("Email")
        root_new.config(bg='grey51')
        #root_new.resizable(0,0)
        senderFrame = LabelFrame(root_new,text="Sender",font=("times new roman", 13, 'bold'), bd=6, bg='grey51', fg='white')
        senderFrame.grid(row=0,column=0, padx=40, pady=20)
        senderLabel = Label(senderFrame,text="Sender Email",font=('times new roman',13,'bold'),bg='grey51',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)
        senderEntry = Entry(senderFrame,font=('times new roman',13,'bold'),bd=2,width=23,relief=GROOVE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passLabel = Label(senderFrame, text="Password", font=('times new roman', 13, 'bold'), bg='grey51',fg='white')
        passLabel.grid(row=1, column=0, padx=10, pady=8)

        passEntry = Entry(senderFrame, font=('times new roman', 13, 'bold'), bd=2, width=23, relief=GROOVE)
        passEntry.grid(row=1, column=1, padx=10, pady=8)

        receiptFrame = LabelFrame(root_new, text="Receipt", font=("times new roman", 13, 'bold'), bd=6, bg='grey51',fg='white')
        receiptFrame.grid(row=1, column=0, padx=40, pady=20)

        revLabel = Label(receiptFrame, text="Email Address", font=('times new roman', 13, 'bold'), bg='grey51', fg='white')
        revLabel.grid(row=0, column=0, padx=10, pady=8)

        revEntry = Entry(receiptFrame, font=('times new roman', 13, 'bold'), bd=2, width=23, relief=GROOVE)
        revEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(receiptFrame, text="Message", font=('times new roman', 13, 'bold'), bg='grey51',fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea=Text(receiptFrame,font=('times new roman',13,'bold'),bd=2,relief=GROOVE,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace("=",'').replace('-',''))

        sendButton=Button(root_new,text='SEND',font=('times new roman',13,'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)

        root_new.mainloop()


def print_bill():
    if textarea.get(1.0,END)=='':
        messagebox.showerror("Error", 'Bill is empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0, END))
        os.startfile(file, 'print')

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == Bill_numberEntry.get():
            f=open(f'bills/{i}', 'r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror("Error", "Invalid bill number")

if os.path.exists('bills'):
    pass
else:
    os.mkdir('bills')


def save_bill():
    global billnumber
    result=messagebox.askyesno("confirm","Do you want to save the bill?")
    if result:
        bill_receipt=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_receipt)
        file.close()
        messagebox.showinfo('Success',f'bill number {billnumber} is saved successfully')
        billnumber=random.randint(1,100)
def bill_menu():
    if nameEntry.get()=='' or PhoneEntry.get()=='':
        messagebox.showerror("Error", "Customer Details Are Required")
    elif cosmeticPriceEntry.get()=='' and groceryPriceEntry.get()=='' and vegitablesPriceEntry.get()=='' and householdPriceEntry.get()=='':
        messagebox.showerror("Error", "No Products Are Selected")
    elif cosmeticPriceEntry.get()=='0 Rs' and groceryPriceEntry.get()=='0 Rs' and vegitablesPriceEntry.get()=='0 Rs' and householdPriceEntry.get()=='0 Rs':
        messagebox.showerror("Error", "No Products Are Selected")
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t****Welcome Customer****\n')
        textarea.insert(END,f'\nBill Number:{billnumber}')
        textarea.insert(END, f'\nCustomer Name:{nameEntry.get()}')
        textarea.insert(END, f'\nPhone Number:{PhoneEntry.get()}')
        textarea.insert(END,'\n=======================================================')
        textarea.insert(END,'Product\t\tQuantity\t\tPrice')
        textarea.insert(END, '\n=======================================================')

        if biscuitEntry.get()!='0':
            textarea.insert(END,f'\nBiscuit\t\t{biscuitEntry.get()}\t\t{biscuitprice} Rs')
        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice\t\t{riceEntry.get()}\t\t{riceprice} Rs')
        if snacksEntry.get()!='0':
            textarea.insert(END,f'\nSnacks\t\t{snacksEntry.get()}\t\t{snacksprice} Rs')
        if drinksEntry.get()!='0':
            textarea.insert(END,f'\nDrinks\t\t{drinksEntry.get()}\t\t{drinksprice} Rs')
        if coffeeEntry.get()!='0':
            textarea.insert(END,f'\nCoffee\t\t{coffeeEntry.get()}\t\t{coffeeprice} Rs')
        if oilEntry.get()!='0':
            textarea.insert(END,f'\nOil\t\t{oilEntry.get()}\t\t{oilprice} Rs')
        if carrotEntry.get()!='0':
            textarea.insert(END,f'\nCarrot\t\t{carrotEntry.get()}\t\t{carrotprice} Rs')
        if onionsEntry.get()!='0':
            textarea.insert(END,f'\nOnions\t\t{onionsEntry.get()}\t\t{onionsprice} Rs')
        if potatoesEntry.get()!='0':
            textarea.insert(END,f'\npotatoes\t\t{potatoesEntry.get()}\t\t{potatoesprice} Rs')
        if radishEntry.get()!='0':
            textarea.insert(END,f'\nRadish\t\t{radishEntry.get()}\t\t{radishprice} Rs')
        if gingerEntry.get()!='0':
            textarea.insert(END,f'\nGinger\t\t{gingerEntry.get()}\t\t{gingerprice} Rs')
        if garlicEntry.get()!='0':
            textarea.insert(END,f'\nGarlic\t\t{garlicEntry.get()}\t\t{garlicprice} Rs')
        if basketEntry.get()!='0':
            textarea.insert(END,f'\nBasket\t\t{basketEntry.get()}\t\t{basketprice} Rs')
        if spoonEntry.get()!='0':
            textarea.insert(END,f'\nSpoon\t\t{spoonEntry.get()}\t\t{spoonprice} Rs')
        if broomEntry.get()!='0':
            textarea.insert(END,f'\nBroom\t\t{broomEntry.get()}\t\t{broomprice} Rs')
        if ladleEntry.get()!='0':
            textarea.insert(END,f'\nLadle\t\t{ladleEntry.get()}\t\t{ladleprice} Rs')
        if trayEntry.get()!='0':
            textarea.insert(END,f'\nTray\t\t{trayEntry.get()}\t\t{trayprice} Rs')
        if jarEntry.get()!='0':
            textarea.insert(END,f'\nJar\t\t{jarEntry.get()}\t\t{jarprice} Rs')
        if lotionEntry.get()!='0':
            textarea.insert(END,f'\nLotion\t\t{lotionEntry.get()}\t\t{lotionprice} Rs')
        if sprayEntry.get()!='0':
            textarea.insert(END,f'\nSpray\t\t{sprayEntry.get()}\t\t{sprayprice} Rs')
        if soapEntry.get()!='0':
            textarea.insert(END,f'\nSoap\t\t{soapEntry.get()}\t\t{soapprice} Rs')
        if gelEntry.get()!='0':
            textarea.insert(END,f'\nGel\t\t{gelEntry.get()}\t\t{gelprice} Rs')
        if handwashEntry.get()!='0':
            textarea.insert(END,f'\nHandwash\t\t{handwashEntry.get()}\t\t{handwashprice} Rs')
        if creamEntry.get()!='0':
            textarea.insert(END,f'\nCream\t\t{creamEntry.get()}\t\t{creamprice} Rs')
        textarea.insert(END, '\n=======================================================')
        if groceryTaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nGrocery Tax\t\t{groceryTaxEntry.get()}')
        if vegitablesTaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nVegitables Tax\t\t{vegitablesTaxEntry.get()}')
        if householdTaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nHousehold Tax\t\t{householdTaxEntry.get()}')
        if cosmeticTaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nCosmetic Tax\t\t{cosmeticTaxEntry.get()}')
        textarea.insert(END,f'\nTotal Bill \t\t{totalbill}')
        textarea.insert(END, '\n=======================================================')
        save_bill()
#function for productprice and tax while clicking each product
def total():
    global biscuitprice,riceprice,snacksprice,drinksprice,coffeeprice,oilprice,carrotprice,onionsprice,potatoesprice,radishprice,gingerprice,garlicprice
    global basketprice,spoonprice,broomprice,ladleprice,trayprice,jarprice,lotionprice,soapprice,sprayprice,gelprice,handwashprice,creamprice,totalbill
    biscuitprice=int(biscuitEntry.get())*50
    riceprice=int(riceEntry.get())*400
    snacksprice=int(snacksEntry.get())*30
    drinksprice=int(drinksEntry.get())*45
    coffeeprice=int(coffeeEntry.get())*40
    oilprice=int(oilEntry.get())*160

    totalgroceryPrice=biscuitprice+riceprice+snacksprice+drinksprice+coffeeprice+oilprice
    groceryPriceEntry.delete(0,END)
    groceryPriceEntry.insert(0,str(totalgroceryPrice)+' Rs')

    grocerytax=totalgroceryPrice*0.18
    groceryTaxEntry.delete(0,END)
    groceryTaxEntry.insert(0,str(grocerytax)+' Rs')

    carrotprice=int(carrotEntry.get())*50
    onionsprice=int(onionsEntry.get())*400
    potatoesprice=int(potatoesEntry.get())*30
    radishprice=int(radishEntry.get())*45
    gingerprice=int(gingerEntry.get())*40
    garlicprice=int(garlicEntry.get())*160

    totalvegitablesPrice=carrotprice+onionsprice+potatoesprice+radishprice+gingerprice+garlicprice
    vegitablesPriceEntry.delete(0,END)
    vegitablesPriceEntry.insert(0,str(totalvegitablesPrice)+' Rs')

    vegitablestax = totalvegitablesPrice*0.18
    vegitablesTaxEntry.delete(0,END)
    vegitablesTaxEntry.insert(0,str(vegitablestax)+' Rs')

    basketprice = int(basketEntry.get()) * 50
    spoonprice = int(spoonEntry.get()) * 400
    broomprice = int(broomEntry.get()) * 30
    ladleprice = int(ladleEntry.get()) * 45
    trayprice = int(trayEntry.get()) * 40
    jarprice = int(jarEntry.get()) * 160

    totalhouseholdPrice = basketprice + spoonprice + broomprice + ladleprice + trayprice + jarprice
    householdPriceEntry.delete(0,END)
    householdPriceEntry.insert(0, str(totalhouseholdPrice) + ' Rs')

    householdtax = totalhouseholdPrice*0.18
    householdTaxEntry.delete(0,END)
    householdTaxEntry.insert(0,str(householdtax)+' Rs')

    lotionprice = int(lotionEntry.get()) * 50
    soapprice = int(soapEntry.get()) * 400
    sprayprice = int(sprayEntry.get()) * 30
    gelprice = int(gelEntry.get()) * 45
    handwashprice = int(handwashEntry.get()) * 40
    creamprice = int(creamEntry.get()) * 160

    totalcosmeticPrice = lotionprice + soapprice + sprayprice + gelprice + handwashprice + creamprice
    cosmeticPriceEntry.delete(0,END)
    cosmeticPriceEntry.insert(0,str(totalcosmeticPrice)+' Rs')

    cosmetictax = totalcosmeticPrice * 0.18
    cosmeticTaxEntry.delete(0,END)
    cosmeticTaxEntry.insert(0,str(cosmetictax)+' Rs')

    totalbill=totalgroceryPrice+totalvegitablesPrice+totalhouseholdPrice+totalcosmeticPrice+grocerytax+vegitablestax+householdtax+cosmetictax



root=Tk()
root.title('Supermarket Billing System')
root.geometry('1270x675')
root.iconbitmap('bill.ico')
headingLabel=Label(root,text='Supermarket Billing System',font=('times new roman',33,'bold'),bg='grey51',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

#customer
customer_details_frame=LabelFrame(root,text="Customer Details",font=('times new roman',13,'bold'),fg='yellow',bd=7,relief=GROOVE,bg='grey51')
customer_details_frame.pack(fill=X,pady=10)

#name
nameLabel=Label(customer_details_frame,text="Name",font=('times new roman',13,'bold'),bg='grey51',fg='white')
nameLabel.grid(row=0,column=0,padx=20)
nameEntry=Entry(customer_details_frame,font=("times new roman",13),bd=6,width=15)
nameEntry.grid(row=0,column=1,padx=7)

#phone
PhoneLabel=Label(customer_details_frame,text="Phone Number",font=('times new roman',13,'bold'),bg='grey51',fg='white')
PhoneLabel.grid(row=0,column=2,padx=20,pady=3)
PhoneEntry=Entry(customer_details_frame,font=("times new roman",13),bd=6,width=15)
PhoneEntry.grid(row=0,column=3,padx=7)

#Billnumber
Bill_numberLabel=Label(customer_details_frame,text="Bill Number",font=('times new roman',13,'bold'),bg='grey51',fg='white')
Bill_numberLabel.grid(row=0,column=4,padx=20,pady=3)
Bill_numberEntry=Entry(customer_details_frame,font=("times new roman",13),bd=6,width=15)
Bill_numberEntry.grid(row=0,column=5,padx=7)

#search button
searchButton=Button(customer_details_frame,text='SEARCH',font=('times new roman',13,'bold'),bd=6,command=search_bill)
searchButton.grid(row=0,column=6,padx=10)

#product
productFrame=Frame(root)
productFrame.pack(pady=10)

#Grocery
groceryFrame=LabelFrame(productFrame,text='Grocery',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=RIDGE,bg='grey51')
groceryFrame.grid(row=0,column=0)

#Grocery items
biscuitLabel=Label(groceryFrame,text='Biscuit',font=('times new roman',13,'bold'),bg='grey51',fg='white')
biscuitLabel.grid(row=0,column=0,pady=9,padx=10)
biscuitEntry=Entry(groceryFrame,font=('times new roman',13,'bold'),width=10,bd=5)
biscuitEntry.grid(row=0,column=1,pady=9,padx=10)
biscuitEntry.insert(0,0)

riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',13,'bold'),bg='grey51',fg='white')
riceLabel.grid(row=1,column=0,pady=9,padx=10)
riceEntry=Entry(groceryFrame,font=('times new roman',13,'bold'),width=10,bd=5)
riceEntry.grid(row=1,column=1,pady=9,padx=10)
riceEntry.insert(0,0)

snacksLabel=Label(groceryFrame,text='Snacks',font=('times new roman',13,'bold'),bg='grey51',fg='white')
snacksLabel.grid(row=2,column=0,pady=9,padx=10)
snacksEntry=Entry(groceryFrame,font=('times new roman',13,'bold'),width=10,bd=5)
snacksEntry.grid(row=2,column=1,pady=9,padx=10)
snacksEntry.insert(0,0)

drinksLabel=Label(groceryFrame,text='Drinks',font=('times new roman',13,'bold'),bg='grey51',fg='white')
drinksLabel.grid(row=3,column=0,pady=9,padx=10)
drinksEntry=Entry(groceryFrame,font=('times new roman',13,'bold'),width=10,bd=5)
drinksEntry.grid(row=3,column=1,pady=9,padx=10)
drinksEntry.insert(0,0)

coffeeLabel=Label(groceryFrame,text='Coffee',font=('times new roman',13,'bold'),bg='grey51',fg='white')
coffeeLabel.grid(row=4,column=0,pady=9,padx=10)
coffeeEntry=Entry(groceryFrame,font=('times new roman',13,'bold'),width=10,bd=5)
coffeeEntry.grid(row=4,column=1,pady=9,padx=10)
coffeeEntry.insert(0,0)

oilLabel=Label(groceryFrame,text='Oil',font=('times new roman',13,'bold'),bg='grey51',fg='white')
oilLabel.grid(row=5,column=0,pady=9,padx=10)
oilEntry=Entry(groceryFrame,font=('times new roman',13,'bold'),width=10,bd=5)
oilEntry.grid(row=5,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

#Vegitables items
vegitablesFrame = LabelFrame(productFrame,text='Vegitables',font=('times new roman', 15, 'bold'),fg='gold',bd=8,relief=RIDGE,bg='grey51')
vegitablesFrame.grid(row=0, column=1)

carrotLabel=Label(vegitablesFrame,text='carrot',font=('times new roman',13,'bold'),bg='grey51',fg='white')
carrotLabel.grid(row=0,column=0,pady=9,padx=10)
carrotEntry=Entry(vegitablesFrame,font=('times new roman',13,'bold'),width=10,bd=5)
carrotEntry.grid(row=0,column=1,pady=9,padx=10)
carrotEntry.insert(0,0)

onionsLabel=Label(vegitablesFrame,text='Onion',font=('times new roman',13,'bold'),bg='grey51',fg='white')
onionsLabel.grid(row=1,column=0,pady=9,padx=10)
onionsEntry=Entry(vegitablesFrame,font=('times new roman',13,'bold'),width=10,bd=5)
onionsEntry.grid(row=1,column=1,pady=9,padx=10)
onionsEntry.insert(0,0)

potatoesLabel=Label(vegitablesFrame,text='Potatoes',font=('times new roman',13,'bold'),bg='grey51',fg='white')
potatoesLabel.grid(row=2,column=0,pady=9,padx=10)
potatoesEntry=Entry(vegitablesFrame,font=('times new roman',13,'bold'),width=10,bd=5)
potatoesEntry.grid(row=2,column=1,pady=9,padx=10)
potatoesEntry.insert(0,0)

radishLabel=Label(vegitablesFrame,text='Radish',font=('times new roman',13,'bold'),bg='grey51',fg='white')
radishLabel.grid(row=3,column=0,pady=9,padx=10)
radishEntry=Entry(vegitablesFrame,font=('times new roman',13,'bold'),width=10,bd=5)
radishEntry.grid(row=3,column=1,pady=9,padx=10)
radishEntry.insert(0,0)

gingerLabel=Label(vegitablesFrame,text='Ginger',font=('times new roman',13,'bold'),bg='grey51',fg='white')
gingerLabel.grid(row=4,column=0,pady=9,padx=10)
gingerEntry=Entry(vegitablesFrame,font=('times new roman',13,'bold'),width=10,bd=5)
gingerEntry.grid(row=4,column=1,pady=9,padx=10)
gingerEntry.insert(0,0)

garlicLabel=Label(vegitablesFrame,text='Garlic',font=('times new roman',13,'bold'),bg='grey51',fg='white')
garlicLabel.grid(row=5,column=0,pady=9,padx=10)
garlicEntry=Entry(vegitablesFrame,font=('times new roman',13,'bold'),width=10,bd=5)
garlicEntry.grid(row=5,column=1,pady=9,padx=10)
garlicEntry.insert(0,0)

#Household items
householdFrame=LabelFrame(productFrame,text='Household',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=RIDGE,bg='grey51')
householdFrame.grid(row=0,column=2)

basketLabel=Label(householdFrame,text='Basket',font=('times new roman',13,'bold'),bg='grey51',fg='white')
basketLabel.grid(row=0,column=0,pady=9,padx=10)
basketEntry=Entry(householdFrame,font=('times new roman',13,'bold'),width=10,bd=5)
basketEntry.grid(row=0,column=1,pady=9,padx=10)
basketEntry.insert(0,0)

spoonLabel=Label(householdFrame,text='Spoon',font=('times new roman',13,'bold'),bg='grey51',fg='white')
spoonLabel.grid(row=1,column=0,pady=9,padx=10)
spoonEntry=Entry(householdFrame,font=('times new roman',13,'bold'),width=10,bd=5)
spoonEntry.grid(row=1,column=1,pady=9,padx=10)
spoonEntry.insert(0,0)

broomLabel=Label(householdFrame,text='Broom',font=('times new roman',13,'bold'),bg='grey51',fg='white')
broomLabel.grid(row=2,column=0,pady=9,padx=10)
broomEntry=Entry(householdFrame,font=('times new roman',13,'bold'),width=10,bd=5)
broomEntry.grid(row=2,column=1,pady=9,padx=10)
broomEntry.insert(0,0)

ladleLabel=Label(householdFrame,text='Ladle',font=('times new roman',13,'bold'),bg='grey51',fg='white')
ladleLabel.grid(row=3,column=0,pady=9,padx=10)
ladleEntry=Entry(householdFrame,font=('times new roman',13,'bold'),width=10,bd=5)
ladleEntry.grid(row=3,column=1,pady=9,padx=10)
ladleEntry.insert(0,0)

trayLabel=Label(householdFrame,text='Tray',font=('times new roman',13,'bold'),bg='grey51',fg='white')
trayLabel.grid(row=4,column=0,pady=9,padx=10)
trayEntry=Entry(householdFrame,font=('times new roman',13,'bold'),width=10,bd=5)
trayEntry.grid(row=4,column=1,pady=9,padx=10)
trayEntry.insert(0,0)

jarLabel=Label(householdFrame,text='Jar',font=('times new roman',13,'bold'),bg='grey51',fg='white')
jarLabel.grid(row=5,column=0,pady=9,padx=10)
jarEntry=Entry(householdFrame,font=('times new roman',13,'bold'),width=10,bd=5)
jarEntry.grid(row=5,column=1,pady=9,padx=10)
jarEntry.insert(0,0)

#cosmetic items
cosmeticFrame=LabelFrame(productFrame,text='Cosmetic',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=RIDGE,bg='grey51')
cosmeticFrame.grid(row=0,column=3)

lotionLabel=Label(cosmeticFrame,text='Lotion',font=('times new roman',13,'bold'),bg='grey51',fg='white')
lotionLabel.grid(row=0,column=3,pady=9,padx=10)
lotionEntry=Entry(cosmeticFrame,font=('times new roman',13,'bold'),width=10,bd=5)
lotionEntry.grid(row=0,column=1,pady=9,padx=10)
lotionEntry.insert(0,0)

soapLabel=Label(cosmeticFrame,text='Soap',font=('times new roman',13,'bold'),bg='grey51',fg='white')
soapLabel.grid(row=1,column=3,pady=9,padx=10)
soapEntry=Entry(cosmeticFrame,font=('times new roman',13,'bold'),width=10,bd=5)
soapEntry.grid(row=1,column=1,pady=9,padx=10)
soapEntry.insert(0,0)

sprayLabel=Label(cosmeticFrame,text='Spray',font=('times new roman',13,'bold'),bg='grey51',fg='white')
sprayLabel.grid(row=2,column=3,pady=9,padx=10)
sprayEntry=Entry(cosmeticFrame,font=('times new roman',13,'bold'),width=10,bd=5)
sprayEntry.grid(row=2,column=1,pady=9,padx=10)
sprayEntry.insert(0,0)

gelLabel=Label(cosmeticFrame,text='Gel',font=('times new roman',13,'bold'),bg='grey51',fg='white')
gelLabel.grid(row=3,column=3,pady=9,padx=10)
gelEntry=Entry(cosmeticFrame,font=('times new roman',13,'bold'),width=10,bd=5)
gelEntry.grid(row=3,column=1,pady=9,padx=10)
gelEntry.insert(0,0)

handwashLabel=Label(cosmeticFrame,text='Hand wash',font=('times new roman',13,'bold'),bg='grey51',fg='white')
handwashLabel.grid(row=4,column=3,pady=9,padx=10)
handwashEntry=Entry(cosmeticFrame,font=('times new roman',13,'bold'),width=10,bd=5)
handwashEntry.grid(row=4,column=1,pady=9,padx=10)
handwashEntry.insert(0,0)

creamLabel=Label(cosmeticFrame,text='Cream',font=('times new roman',13,'bold'),bg='grey51',fg='white')
creamLabel.grid(row=5,column=3,pady=9,padx=10)
creamEntry=Entry(cosmeticFrame,font=('times new roman',13,'bold'),width=10,bd=5)
creamEntry.grid(row=5,column=1,pady=9,padx=10)
creamEntry.insert(0,0)

#bill
billframe=Frame(productFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=4,padx=10)

billareaLabel=Label(billframe,text='Bill Section',font=('times new roman',13,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

#scrolling
scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=RIDGE,bg='grey51')
billmenuFrame.pack()
billnumber=random.randint(1,100)

#price of product
groceryPriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman',13,'bold'),bg='grey51',fg='white')
groceryPriceLabel.grid(row=0,column=0,pady=9,padx=10)
groceryPriceEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
groceryPriceEntry.grid(row=0,column=1,pady=9,padx=10)

vegitablesPriceLabel=Label(billmenuFrame,text='Vegitables Price',font=('times new roman',13,'bold'),bg='grey51',fg='white')
vegitablesPriceLabel.grid(row=1,column=0,pady=9,padx=10)
vegitablesPriceEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
vegitablesPriceEntry.grid(row=1,column=1,pady=9,padx=10)

householdPriceLabel=Label(billmenuFrame,text='Household Price',font=('times new roman',13,'bold'),bg='grey51',fg='white')
householdPriceLabel.grid(row=2,column=0,pady=9,padx=10)
householdPriceEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
householdPriceEntry.grid(row=2,column=1,pady=9,padx=10)

cosmeticPriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',13,'bold'),bg='grey51',fg='white')
cosmeticPriceLabel.grid(row=3,column=0,pady=9,padx=10)
cosmeticPriceEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
cosmeticPriceEntry.grid(row=3,column=1,pady=9,padx=10)

#tax of product
groceryTaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman',13,'bold'),bg='grey51',fg='white')
groceryTaxLabel.grid(row=0,column=2,pady=9,padx=10)
groceryTaxEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
groceryTaxEntry.grid(row=0,column=4,pady=9,padx=10)

vegitablesTaxLabel=Label(billmenuFrame,text='Vegitables Tax',font=('times new roman',13,'bold'),bg='grey51',fg='white')
vegitablesTaxLabel.grid(row=1,column=2,pady=9,padx=10)
vegitablesTaxEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
vegitablesTaxEntry.grid(row=1,column=4,pady=9,padx=10)

householdTaxLabel=Label(billmenuFrame,text='Household Tax',font=('times new roman',13,'bold'),bg='grey51',fg='white')
householdTaxLabel.grid(row=2,column=2,pady=9,padx=10)
householdTaxEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
householdTaxEntry.grid(row=2,column=4,pady=9,padx=10)

cosmeticTaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',13,'bold'),bg='grey51',fg='white')
cosmeticTaxLabel.grid(row=3,column=2,pady=9,padx=10)
cosmeticTaxEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
cosmeticTaxEntry.grid(row=3,column=4,pady=9,padx=10)

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=5,rowspan=3)

#totalbutton
totalButton=Button(buttonFrame,text='Total',font=('times new roman',16,'bold'),bg='grey51',fg='white',bd=5,width=8,pady=6,command=total)
totalButton.grid(row=0,column=0)

billButton=Button(buttonFrame,text='Bill',font=('times new roman',16,'bold'),bg='grey51',fg='white',bd=5,width=8,pady=6,command=bill_menu)
billButton.grid(row=0,column=1)

emailButton=Button(buttonFrame,text='Email',font=('times new roman',16,'bold'),bg='grey51',fg='white',bd=5,width=8,pady=6,command=send_email)
emailButton.grid(row=0,column=2)

printButton=Button(buttonFrame,text='Print',font=('times new roman',16,'bold'),bg='grey51',fg='white',bd=5,width=8,pady=6,command=print_bill)
printButton.grid(row=0,column=3)

clearButton=Button(buttonFrame,text='Clear',font=('times new roman',16,'bold'),bg='grey51',fg='white',bd=5,width=8,pady=6)
clearButton.grid(row=0,column=4)







root.mainloop()