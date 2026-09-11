import pandas as pd

df = pd.read_csv("cupcake_sales_practice.csv") #creating df and reading our .csv file allowing us to standardize, clean and perform math on it.

df["flavor"] = df["flavor"].str.strip().str.lower() #stripping whitespace and making everything lowercase

# this flavor map allows us to remap a finite amount of flavors. All individual flavors converge to their corresponding flavor
flavor_map = {
    "carrot":"Carrot Cake",
    "carrot cake cupcake": "Carrot Cake",
    "carrot cake": "Carrot Cake",
    
    
    "vanilla": "Vanilla",
    "vanilla cupcake": "Vanilla",
    "vanila": "Vanilla",
    
    "funfetti": "Funfetti",
    "fun fetti": "Funfetti",
    "funfetti cupcake": "Funfetti",
    
    "lemon": "Lemon",
    "lemon cupcake": "Lemon",
    
    "chocolate cupcake": "Chocolate",
    "choc": "Chocolate",
    "chocolate": "Chocolate",
    
    "red velvet": "Red Velvet",
    "red velvet cupcake": "Red Velvet",
    "redvelvet": "Red Velvet",
}

    

print (df.head())
print(df.info())

df["flavor"] = df["flavor"].replace(flavor_map) #replacing with our newly updated flavor map
print(df["flavor"].unique())

df=df.dropna(subset=["flavor"]) #removes empty rows
print(df["flavor"].unique())
print(df.shape)


#for unit price column.
#We want to look at the data before standardizing.
print(df["unit_price"].unique())

df["unit_price"]= df["unit_price"].str.strip() #stripping whitespace
df["unit_price"] = df["unit_price"].str.replace("$","") #stripping $ signs

print(df["unit_price"].unique()) #making sure that it stripped $ signs

df["unit_price"] = df["unit_price"].astype(float) #we want to convert all these spreadhseet entries into actual data types. we need datatype float64, we use pythons built in "float".

print(df["unit_price"].sum()) #printing the sum of all floats
print(df["unit_price"].info()) #checking the datatype


outliers = df[(df["unit_price"] <1) | (df["unit_price"] >10)] #creating a varaible called outliers that takes the outliers based on a certain range. range here is <1, >10
print(outliers)

df = df[(df["unit_price"] >1) & (df["unit_price"] < 10)] #opposite of outliers.taking data we want by specifying a range between 1-10
print(df)

print("-----------------------------------------------------------------------------")
print(df.shape) #.shape gives rows x columns


df["order_date"] = pd.to_datetime(df["order_date"], format= "mixed")
print(df["order_date"].head(20))
print(df.info())


df = df.dropna(subset=["quantity"]) #getting rid of empty rows

print(df["quantity"].isna().sum()) #checking to see if theres any entries in quantity that are empty, we are also summing those empty entries. uses TRUE, FALSE logic
print(df.shape) #seeing how many many rows x columns we have now

#-----------------------------------------------------------------creating new variables and columns to our data sheet -------------------------------------------------------------

df["revenue"]=  (df["quantity"]) * (df["unit_price"]) #creating a new column called "revenue", which equals quantity * price
print(df[["flavor","quantity","unit_price","revenue"]].head(10)) #printing out our data with flavor, quantity, unit_price, revenue
print("revenue by flavor")
print(df.groupby("flavor")["revenue"].sum()) #groupby flavor an revenue

df["month"] = df["order_date"].dt.month

print(df.groupby("month")["revenue"].sum()) #grouping by month, taking the sum of all entries 

print(df["revenue"].mean())


print(df.groupby("order_date")["revenue"].sum().max()) #taking the best day,the day the most money was made




#pushing to excel sheet
with pd.ExcelWriter("cupcake_analysis.xlsx") as writer:
    df.to_excel(writer, sheet_name="Cleaned Data", index=False)
    df.groupby("flavor")["revenue"].sum().to_excel(writer, sheet_name="Revenue by Flavor")
    df.groupby("month")["revenue"].sum().to_excel(writer, sheet_name="Revenue by Month")