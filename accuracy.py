from rouge import Rouge
ROUGE = Rouge()
reference='''Napoleon Hill is the most famous conman you ve probably never heard of
Born into poverty in rural Virginia at the end of the   th century  Hill went on to write one of the most successful self help books of the   th century  Think and Grow Rich
In fact  he helped invent the genre
But it s the untold story of Hill s fraudulent business practices  tawdry sex life  and membership in a New York cult that makes him so fascinating
That cult would become infamous in the late     s for trying to raise an  immortal baby   But even those who know the story of Immortal Baby Jean may not know that the cult was inspired by Hill s teachings  practically using his most famous work as their holy text
Don t worry  the whole story of Napoleon Hill only gets weirder from there
Modern readers are probably familiar with the      sensation The Secret  but the concepts in that book were essentially plagiarized from Napoleon Hill s      classic Think and Grow Rich  which has reportedly sold over    million copies to date
The big idea in both  The material universe is governed quite directly by our thoughts
If you simply visualize what you want out of life  those things and more will be delivered to you
Especially if those things involve money
He really did live an extraordinary life  just not the life that his thousands of disciples over the years have claimed
It s just too bad that Hill spent most of his life as an utter fraud a fraud who by hook and by crook was constantly reinventing himself      
Napoleon Hill s Wikipedia page sometimes warns that it s written like an advertisement
Which pretty much hits the nail on the head
Hill s entire life was an advertisement  one that spoke of honor and taught that if people visualized their dreams and narrowed down their own purpose in life  good things would come to them
And if the lessons in Hill s writings  work  for some people  I say good for them
I m not here to say that there s nothing to be learned from some of Hill s writings especially those that speak of self confidence  being kind to others  and going the extra mile for something you believe in
But the real story behind Napoleon Hill s life is long past due
After countless hours of research  I still feel like I ve captured just a mere glimpse of the complex man that was Napoleon Hill'''
candidate='''Napoleon Hill is the most famous conman you ve probably never heard of
Born into poverty in rural Virginia at the end of the   th century  Hill went on to write one of the most successful self help books of the   th century  Think and Grow Rich
In fact  he helped invent the genre
But it s the untold story of Hill s fraudulent business practices  tawdry sex life  and membership in a New York cult that makes him so fascinating
That cult would become infamous in the late     s for trying to raise an  immortal baby   But even those who know the story of Immortal Baby Jean may not know that the cult was inspired by Hill s teachings  practically using his most famous work as their holy text
Don t worry  the whole story of Napoleon Hill only gets weirder from there
Modern readers are probably familiar with the      sensation The Secret  but the concepts in that book were essentially plagiarized from Napoleon Hill s      classic Think and Grow Rich  which has reportedly sold over    million copies to date
The big idea in both  The material universe is governed quite directly by our thoughts
If you simply visualize what you want out of life  those things and more will be delivered to you
Especially if those things involve money
He really did live an extraordinary life  just not the life that his thousands of disciples over the years have claimed
It s just too bad that Hill spent most of his life as an utter fraud a fraud who by hook and by crook was constantly reinventing himself      
Napoleon Hill s Wikipedia page sometimes warns that it s written like an advertisement
Which pretty much hits the nail on the head
Hill s entire life was an advertisement  one that spoke of honor and taught that if people visualized their dreams and narrowed down their own purpose in life  good things would come to them
And if the lessons in Hill s writings  work  for some people  I say good for them
I m not here to say that there s nothing to be learned from some of Hill s writings especially those that speak of self confidence  being kind to others  and going the extra mile for something you believe in
But the real story behind Napoleon Hill s life is long past due
After countless hours of research  I still feel like I ve captured just a mere glimpse of the complex man that was Napoleon Hill'''
print(ROUGE.get_scores(candidate, reference))
