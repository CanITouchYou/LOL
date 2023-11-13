from requests_html import HTMLSession
import pandas as pd
s = HTMLSession()
data = []
update_time = '&sp=CAI%253D'

def getURL(topic, scroll_down, file_name): #scroll_down
    
    # topic = 'LOL'
    url = 'https://www.youtube.com/results?search_query='+topic+update_time
    # print(url)
    
    # vid_title = topic + '的搜尋結果'
    # vid_url = url 
    # data.append([vid_title, vid_url])
    
    # print('start get')
    r = s.get(url)
    # print(r)
    print('start render..')
    r.html.render(sleep = 3, timeout = 100, keep_page = True, scrolldown = int(scroll_down))
    print('done render')
    container = r.html.find('ytd-video-renderer.style-scope.ytd-item-section-renderer')
    # print('done get')

    # print('start for')
    for elem in container :
        vid_title = elem.find('yt-formatted-string.style-scope.ytd-video-renderer', first = True).text
        # print(vid_title)
        vid_url = 'https://www.youtube.com' + elem.find('a#video-title', first = True).attrs['href']
        data.append([vid_title, vid_url])
    # print('done for loop')
    
    df = pd.DataFrame(data, columns=['V_title', 'V_url'])
    df.to_csv(file_name+'.csv',index=False)
    # print('done')

i_topic = input('input topic : ') # %23LOL = #LOL
i_sd = input('input scrolltime : ')
i_filename = input('input file name : ') # >20
# print(i_topic + i_sd+ i_filename)
getURL(i_topic,i_sd,i_filename)
print('DONE')


