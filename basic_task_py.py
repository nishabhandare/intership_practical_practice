#1. hello world ... by  YOUR_NAME
print("Q1")
print("Hello World... by Nisha")

#2. create 2 variables cost_price , selling_price and calculate the profit or loss
print("\nQ2")
cost_price=500
selling_price=700
profit= (selling_price - cost_price)
loss= (cost_price - selling_price)
print("Cost prize: ",cost_price)
print("Selling prize: ",selling_price)
print("Profit: ",profit)
print("Loss: ",loss)

#3. WAP to check wheather the num is odd or even
print("\nQ3")
num=10
if num % 2 ==0 :
    print(num,"is Even.")
else:
    print(num,"is Odd.")

#4. WAP to check weather the age is valid and elegible for voting or not
print("\nQ4")
age=20
if age >= 18:
    print("elegible for voting, age is ",age)
else:
    print("Not elegible for voting, age is ",age)

#5. WAP to find the word1 and word2 is Anagram or Not
print("\nQ5")
word1="listen"
word2="silent"
if sorted(word1) == sorted(word2):
    print("Anagram") 
else: 
    print("Not Anagram") 