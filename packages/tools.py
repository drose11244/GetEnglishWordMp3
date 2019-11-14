import datetime
import os
import sys


def get_date():
    time = datetime.datetime.now()
    year = time.year
    month = time.month
    day = time.day
    hour = time.hour
    mins = time.minute
    second = time.second
    getTimeNow = str(year) + str(month) + str(day) + \
        str(hour) + str(mins) + str(second)
    return getTimeNow


def show_where():
    print("show_where: sys.argv[0] is", repr(sys.argv[0]))
    print("show_where: __file__ is", repr(__file__))
    print("show_where: cwd is", repr(os.getcwd()))
    return


def get_platform():
    platforms = {
        'aix': 'AIX',
        'linux': 'Linux',
        'darwin': 'macOS',
        'win32': 'Windows',
        'cygwin': 'Windows/Cygwin',
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]


cookies = {
    'XSRF-TOKEN': 'd8212e83-98e4-4a7c-b5d5-a74e3824923f',
    'amp-access': 'amp-XaQphVk46Ug6CLyhJYoxBg',
    'preferredDictionaries': 'english-chinese-traditional,english-chinese-simplified,english,british-grammar',
    '_ga': 'GA1.3.2124830091.1573182452',
    '_gid': 'GA1.3.1171566713.1573182452',
    '_gat': '1',
    '_fbp': 'fb.1.1573182452379.1914471282',
    '__gads': 'ID=19307f7324460004:T=1573182448:S=ALNI_MbXZc4DuuIUjHXrnZmdR0HNknlqwg',
    'cto_lwid': '2ffd11ae-7825-48d6-bf81-212f6b90215d',
    'cto_bundle': 'c-vKWV83RzQxUUIyRU0zeE1kVFhaUFluZ1JtMWIlMkZPcHByVDdDelYzRlklMkZOenIlMkZTdDRGUWZBOGxBSHclMkJ3UkpiZHRYQ1VYdURVNFVZdVBwY2ZUVHNOUWpyN1Q4UnhxaXJ6OFEwU0R2TUtkUldCajMxQkFubld6S3VITkN1YU1Mck1ibTBUTTlmbmZYYyUyQjVlVnk5d1pGemxXNEFnJTNEJTNE',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Accept': 'audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5',
    'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/acrobatic',
    'Range': 'bytes=0-',
    'Connection': 'keep-alive',
}

output_file_name = 'output/'


if get_platform() == 'Linux':
    current_path = os.getcwd()
    main_folder = './' + output_file_name

if get_platform() == 'macOS':

    # Executable
    path = sys.argv[0]
    get_baseName_position = path.rfind('/')
    get_kill_word = -len(path[get_baseName_position:])
    current_path = path[:get_kill_word]
    main_folder = current_path + '/' + output_file_name

    # Directly to execute file
    # current_path = os.getcwd()
    # main_folder = current_path + '/' +output_file_name


dictitionaryHeaders = 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/'
