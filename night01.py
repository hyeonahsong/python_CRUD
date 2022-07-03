# List => [1, 2, 3, 4]
# Tuple => (1, 2, 3, 4)
# tuple은 수정 불가!
# Dictionary => {key: value, key: value}
# Set => {1, 2, 3, 4}

# dic => list

music_list = []

def input():
    title = input("제목을 입력하세요.")
    singer = input("가수명을 입력하세요.")
    long = input("노래의 길이를 입력하세요.")

    music = {"title":title, "singer":singer, "long":long}
    music_list.append(music)

def output():
    for music_data in music_list:
        print(music_data)


def search():
    search_input = input("검색 할 제목을 입력하세요.")

    for music_data in music_list:
        if music_data.get('title') == search_input:
            print(music_data)


def modify():
    search_title = input("수정 할 곡의 제목을 입력하세요.")

    for music_data in music_list:
        if music_data.get('title') == search_title:
            music_data["title"] = input("수정 할 제목을 입력하세요.")
            music_data["singer"] = input("수정 할 곡의 가수명을 입력하세요.")
            music_data["long"] = input("수정 할 곡의 길이를 입력하세요.")


def delete():
    delete_title = input("삭제 할 곡의 제목을 입력하세요.")

    for music_data in music_list:
        if music_data.get('title') == delete_title:
            music_list.remove(music_data)


if __name__ == '__main__':
    input()
    search()
    modify()
    output()
    delete()

