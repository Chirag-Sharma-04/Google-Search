import webbrowser as wb
#pip install google 

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
query =(input("What would u like to search: "))
 
for j in search(query, tld="co.in", num=1, stop=1, pause=0):
    print(j)
url1=j
wb.get().open_new(url1)
