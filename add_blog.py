import re as r
template = open("blog/ecsc.html",mode="r").readlines()
pattern = '<div class="blog-content scene_element scene_element--fadein">'
content_begin_num = 0
content_end_num = 0
content_begin_found = False
content_title_block_begin_num = 0
content_title_block_end_num = 0
content_title_block_begin_found = False
for line in enumerate(template):
    if '<div class="blog-title scene_element scene_element--fadeinleft">' in line[1]:
        content_title_block_begin_num = line[0]
        content_title_block_begin_found = True
    if '<div class="blog-content scene_element scene_element--fadein">' in line[1]:
        content_begin_num = line[0]
        content_begin_found = True
    if "</div>" in line[1] and content_title_block_begin_found:
        content_title_block_end_num = line[0]
        content_title_block_begin_found = False
    if "</div>" in line[1] and content_begin_found:
        content_end_num = line[0]
        content_begin_found = False

content_title_block = template[content_title_block_begin_num+1:content_title_block_end_num]
content = template[content_begin_num+1:content_end_num]

new_content = []
condition = False
while not condition:
    new_content.append(" "*14 + input("New content new line: "))
    condition = "END" in new_content[-1]
new_content = new_content[:-1]
new_title = input("New title: ")
new_subtitle = input("New subtitle: ")
#print("".join(content_title_block))
content_title_block[2] = " "*14 + new_title + "\n"
content_title_block[5] = " "*14 + new_subtitle + "\n"
#print("".join(content_title_block))

for line in range(content_begin_num, content_end_num+1):
    template[line] = new_content[line - content_begin_num]

for line in range(content_title_block_begin_num, content_title_block_end_num+1):
    template[line] = content_title_block[line - content_title_block_begin_num]

print("".join(template))