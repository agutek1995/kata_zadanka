def domain_name(url):
    pass
    if 'www' in url:
        n=url.index('.')
        domena=''
        for i in url[(n+1):]:
            if i=='.':
                break
            domena=domena+i
        return(domena)
    elif '//' in url:
        n = url.index("/")
        domena = ''
        for i in url[(n + 2):]:
            if i == '.':
                break
            domena = domena + i
        return(domena)
    else:
        domena = ''
        for i in url:
            if i == '.':
                break
            domena = domena + i
        return (domena)

domain_name("http://www.zombie-bites.com")
domain_name("http://github.com/carbonfive/raygun")
