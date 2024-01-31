## Foreword

(Sourced from my solution to the challenge [*Book_recommendation_engine_using_KNN*](https://github.com/GBlanch/fCC-Machine-Learning-with-Python-Certification/blob/main/2.book_recommendation_engine_using_knn/fcc_book_recommendation_knn_dec30.ipynb))


> ### On some preferable practices of problem solving when coding
>
> As similarly occurred to me when solving the challenges for the course _fCC DA with Python_, the cornerstone to tackle and solve these problems was to commence by **understanding** the **test_module** and its classes and methods. In the case of this ML course, since an IDE is being used to develop and test all the code, it's about [understanding the **test_function**](#understanding-the-test-function).
>
> Another noteworthy habit that helped me organize and map what I was coding was to utilize constants and variables as much as conveniently possible. That also helped me tweak my code and re-plan my steps when facing dead ends in my initial mapping or when encountering inescapable Exceptions.
>
> Nonetheless, and prior to taking any small reverse engineering approach, I tried to stay up-close to some key principles which are a _sine qua non_ requisites in each and every project, whatever their size and scope can be. These are **understanding the problem statement** - to the extent as though _you created it_ - , **exploring** and **becoming oneself familiar with the provided datasets**.
> 
> Thanks for reading this and happy coding!



## Problems

  - ### [Rock Paper Scissors](https://replit.com/@gblandugar/boilerplate-rock-paper-scissors#RPS.py)
  - ### [Cat and Dog Image Classifier](https://github.com/GBlanch/fCC-Machine-Learning-with-Python-Certification/tree/main/1.cat_and_dog_image_classifier)
  - ### [Book Recommendation Engine using KNN](https://github.com/GBlanch/fCC-Machine-Learning-with-Python-Certification/tree/main/2.book_recommendation_engine_using_knn)
  - ### [Linear Regression Health Costs Calculator](https://github.com/GBlanch/fCC-Machine-Learning-with-Python-Certification/tree/main/3.linear_regression_health_costs_calc)
  - ### [Neural Network SMS Text Classifier](https://github.com/GBlanch/fCC-Machine-Learning-with-Python-Certification/blob/main/4.neural_network_sms_text_classifier/fcc_sms_text_classification.ipynb)

<br>

--- 

## Understanding-the-test-function


```python
books = get_recommends("Where the Heart Is (Oprah's Book Club (Paperback))")
print(books)

def test_book_recommendation():
  test_pass = True
  recommends = get_recommends("Where the Heart Is (Oprah's Book Club (Paperback))")
  if recommends[0] != "Where the Heart Is (Oprah's Book Club (Paperback))":
    test_pass = False
  recommended_books = ["I'll Be Seeing You", 'The Weight of Water', 'The Surgeon', 'I Know This Much Is True']
  recommended_books_dist = [0.8, 0.77, 0.77, 0.77]
  for i in range(2):
    if recommends[1][i][0] not in recommended_books:
      test_pass = False
    if abs(recommends[1][i][1] - recommended_books_dist[i]) >= 0.05:
      test_pass = False
  if test_pass:
    print("You passed the challenge! 🎉🎉🎉🎉🎉")
  else:
    print("You haven't passed yet. Keep trying!")

test_book_recommendation()

["Where the Heart Is (Oprah's Book Club (Paperback))", [["I'll Be Seeing You", 0.8016], ['The Weight of Water', 0.7709], ['The Surgeon', 0.7699], ['I Know This Much Is True', 0.7677]]]
You passed the challenge! 🎉🎉🎉🎉🎉
```

The variable `recommends` which is being tested in the function *test_book_recommendation()* , must be a nested list and it has to satisfy, at least but not limited to, the following:

- the first element must be the title (str) of the book being tested. (L7) (*'Where the Heart Is'*)
- the second element must be another nested list - of at least 4 dimensions - , and inside each sublist:
    - the first parameter must be the title of a book (str) and each parameter must be equal to the elements (str) of the list `recommended_books`. 
    - the second parameter must be the distance(int) of the k-nearest neighbors of each book. The values of the elements (int) of the list `recommended_books_dist` will be subtracted to the ones of each parameter from `recommends`, and for each index (these have no limit) the absolute value of this difference (int) must be equal or smaller than .05 .(L14)


[Back to Foreword](#foreword)
<br>

## Proof of completion


![Machine Learning Developer Certification](https://raw.githubusercontent.com/GBlanch/fCC-Machine-Learning-with-Python-Certification/main/ML_Developer_certification.png)

[Verify this certification](https://www.freecodecamp.org/certification/GBlanch/machine-learning-with-python-v7)

