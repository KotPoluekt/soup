import re

from bs4 import BeautifulSoup

with open("blank/index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

# title = soup.title.text
# print(title)

# find find_all
# page_h1 = soup.find('h1')
# print(page_h1.text)

# page_all_h1 = soup.find_all('h1')
# print(page_all_h1)
# for h1 in page_all_h1:
#     print(h1.text)

# user_name = soup.find(class_='user__name').find('span').text
# print(user_name)

# user_name = soup.find('div', class_='user__name').find('span').text
# print(user_name)

# user_name = soup.find('div', {"class": "user__name", "id": "id1"})
# print(user_name)

# spans_in_user_data = soup.find('div', class_="user__data").find_all('span')
# print(spans_in_user_data)

# all_links = soup.find_all('a')
#
# for link in all_links:
#     print(link.text)
#     print(link.get('href'))


# find_parent find_parents
# post_div = soup.find(class_="post__text").find_parent()
# print(post_div)

# post_div = soup.find(class_="post__text").find_parent("div", "user__post")
# print(post_div)

# post_divs = soup.find(class_="post__text").find_parents("div", "user__post")
# print(post_divs)



# .next_element prev_element
# next_el = soup.find(class_="post__title").next_element.next_element.next_element
# print(next_el)

# next_el = soup.find(class_="post__title").find_next()
# print(next_el)

# find_next_sibling find_previous_sibling
# next_sib = soup.find(class_="post__title").find_next_sibling()
# print(next_sib)




# link = soup.find(class_='user__avatar').find('img')
# print(link.get("src"))
# print(link["src"])


# find_a_by_text = soup.find("a", text="Одежда для взрослых")
# print(find_a_by_text['href'])

# find_a_by_text = soup.find("a", text=re.compile("Одежда"))
# print(find_a_by_text)

find_all_clothes = soup.find_all(text=re.compile("[Оо]дежда"))
print(find_all_clothes)