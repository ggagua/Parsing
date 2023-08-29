ამ პროექტში მოგვაქვს ალტას საიტიდან ყველაზე ძვირადღირებული 40 სმარტფონი (5 გვერდი) პითონის BeautifulSoup მოდულის საშუალებით, ასევე ვიყენებთ sqlite3 
მოდულს, random და sleep მოდულებს, სმარტფონების სექციაში ვაკითხავთ ფასსა და სმარტფონის სახელს და მოგვაქვს ინფორმაცია request მოდულის საშუალებით, 
რომელსაც შემდეგ ვამატებთ sql ბაზაში, კოდში გათვალისწინებულია pagination, ანუ, შეგვიძლია განვსაზღვროთ რამდენი გვერდიდან გვინდა ინფორმაციის წამოღება,
ამ შემთხვევაში პირველი 5 გვერდის მონაცემებია შეტანილი. (სორტირება გაკეთებულია პირდაპირ საიტზევე და პირდაპირ სორტირებულად მომაქვს/შემაქვს data).
სხვა დეტალები პითონის კოდშია გაწერილი კომენტარების სახით.


In this project, we fetch the top 40 most expensive smartphones from Alta's site (5 pages) via Python's BeautifulSoup library, and we also use sqlite3
We ask the module, random and sleep modules, in the smartphone section for the price and the name of the smartphone, and we get information through the request module.
which we then add to the sql base.
