```python
# डेटा प्रकार का उदाहरण
# 
# @लेखक SunilOS  
# @संस्करण 1.0
# @कॉपीराइट (c) SunilOS  
# @Url www.SunilOs.com

# पूर्णांक संख्या (Integer Numbers)
a = 100  # 'a' नाम के वेरिएबल को 100 की संख्या दी गई
ids = 101  # 'ids' नाम के वेरिएबल को 101 की संख्या दी गई
price = 99.99  # 'price' नाम के वेरिएबल को 99.99 का मान (दशमलव संख्या) दिया गया

# पूर्णांक और दशमलव संख्या प्रिंट करें
print(a)  
print(ids)  
print(price)  

# दशमलव संख्या (floating-point)
x = 10.5  # 'x' को 10.5 का मान दिया गया
y = 5     # 'y' को 5 का मान दिया गया

# टाइप कास्टिंग (प्रकार बदलना) का उदाहरण
print(x + y)  # बिना प्रकार बदले 'x' और 'y' को जोड़ें (दशमलव परिणाम)
print(int(x) + y)  # 'x' को पूर्णांक में बदलकर जोड़ें (पूर्णांक परिणाम)

# सूची (List) के उदाहरण
list1 = ['a', 'b', 'c', 'd', 'e']  # अक्षरों की सूची
list2 = [1, 2, 3, 4, 5]  # संख्याओं की सूची

# दो सूचियों को मिलाना
list3 = list1 + list2  # list1 और list2 को मिलाकर नई सूची बनाएं

# सूची को दोहराना
list4 = list1 * 2  # list1 के तत्वों को दो बार दोहराएं

# उप-सूची निकालना
list5 = list1[2:3]  # सूची से दूसरे से तीसरे तत्व (तीसरा तत्व छोड़कर) तक की उप-सूची
list6 = list1[2:]   # सूची के दूसरे तत्व से आखिरी तक की उप-सूची

# सूचियों को प्रिंट करें
print(list1)  
print(list2)  
print(list3)  
print(list4)  

# सूची की लंबाई
print(len(list1))  # list1 में कितने तत्व हैं यह बताता है

# विशेष तत्व प्रिंट करना
print(list1[1])  # list1 के पहले (index 1) तत्व को प्रिंट करता है ('b')

# सूची के तत्व को बदलना
list1[1] = 'BB'  # list1 के पहले तत्व को 'BB' से बदलता है
print(list1[1])  # बदले गए पहले तत्व को प्रिंट करें

# सूची से तत्व हटाना
del list1[1]  # list1 के पहले तत्व को हटा देता है
print(list1)  # हटाने के बाद list1 को प्रिंट करें
```

