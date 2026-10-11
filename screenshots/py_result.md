D:\Pycharmcommunity2025\PythonProject2\.venv\Scripts\python.exe D:\Pycharmcommunity2025\PythonProject2\my_agent.py 
2026-10-11 21:17:10,094 - world-intel-mcp - INFO - World Intelligence MCP Server starting (132 tools)
2026-10-11 21:17:10,094 - world-intel-mcp.vector-store - INFO - Vector store worker started
2026-10-11 21:17:10,094 - world-intel-mcp - INFO - Vector store worker started
2026-10-11 21:17:10,116 - mcp.server.lowlevel.server - INFO - Processing request of type ListToolsRequest
成功连接工具: intel_daily_digest
模型打算调用: ```json
{"tool": "intel_daily_digest", "arguments": {"keywords": "financial systems network attack", "time_range": "24h"}}
```
2026-10-11 21:17:23,158 - mcp.server.lowlevel.server - INFO - Processing request of type CallToolRequest
2026-10-11 21:17:23,159 - world-intel-mcp - INFO - Tool call: intel_daily_digest({"keywords": "financial systems network attack", "time_range": "24h"})
2026-10-11 21:17:34,911 - httpx - INFO - HTTP Request: GET https://therecord.media/feed "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:35,097 - httpx - INFO - HTTP Request: GET https://www.cisa.gov/cybersecurity-advisories/all.xml "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:35,169 - httpx - INFO - HTTP Request: GET https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json "HTTP/1.1 200 OK"
2026-10-11 21:17:35,170 - httpx - INFO - HTTP Request: GET https://www.schneier.com/feed/atom/ "HTTP/1.1 200 OK"
2026-10-11 21:17:35,172 - httpx - INFO - HTTP Request: GET https://techcrunch.com/feed/ "HTTP/1.1 200 OK"
2026-10-11 21:17:35,201 - httpx - INFO - HTTP Request: GET https://www.who.int/rss-feeds/news-english.xml "HTTP/1.1 200 OK"
2026-10-11 21:17:35,210 - httpx - INFO - HTTP Request: GET https://www.france24.com/en/rss "HTTP/1.1 200 OK"
2026-10-11 21:17:35,227 - httpx - INFO - HTTP Request: GET https://www.bleepingcomputer.com/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:35,229 - httpx - INFO - HTTP Request: GET https://services.swpc.noaa.gov/products/alerts.json "HTTP/1.1 200 OK"
2026-10-11 21:17:35,279 - httpx - INFO - HTTP Request: GET https://opensky-network.org/api/states/all "HTTP/1.1 200 "
2026-10-11 21:17:35,282 - httpx - INFO - HTTP Request: GET https://ucdpapi.pcr.uu.se/api/gedevents/25.1?pagesize=100&page=0 "HTTP/1.1 401 Unauthorized"
2026-10-11 21:17:35,484 - httpx - INFO - HTTP Request: GET https://tools.cdc.gov/api/v2/resources/media/132608.rss "HTTP/1.1 200 OK"
2026-10-11 21:17:35,517 - httpx - INFO - HTTP Request: GET https://services.swpc.noaa.gov/json/goes/primary/xrays-6-hour.json "HTTP/1.1 200 OK"
2026-10-11 21:17:35,670 - httpx - INFO - HTTP Request: GET https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.json "HTTP/1.1 200 OK"
2026-10-11 21:17:35,674 - httpx - INFO - HTTP Request: GET https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=4.5&orderby=time&limit=50&starttime=2026-10-10T13%3A17%3A23 "HTTP/1.1 200 OK"
2026-10-11 21:17:35,675 - httpx - INFO - HTTP Request: GET https://urlhaus-api.abuse.ch/v1/urls/recent/limit/25/ "HTTP/1.1 401 Unauthorized"
2026-10-11 21:17:35,726 - httpx - INFO - HTTP Request: GET https://isc.sans.edu/api/topips/records/20?json "HTTP/1.1 200 OK"
2026-10-11 21:17:36,077 - httpx - INFO - HTTP Request: GET https://api.adsb.lol/v2/mil "HTTP/1.1 200 OK"
2026-10-11 21:17:36,078 - httpx - INFO - HTTP Request: GET https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=science "HTTP/1.1 200 OK"
2026-10-11 21:17:36,130 - httpx - INFO - HTTP Request: GET https://phys.org/rss-feed/ "HTTP/1.1 200 OK"
2026-10-11 21:17:36,303 - httpx - INFO - HTTP Request: GET https://www.twz.com/feed "HTTP/1.1 200 OK"
2026-10-11 21:17:36,488 - httpx - INFO - HTTP Request: GET https://spacenews.com/feed/ "HTTP/1.1 200 OK"
2026-10-11 21:17:36,497 - httpx - INFO - HTTP Request: GET https://news.usni.org/feed "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:36,531 - httpx - INFO - HTTP Request: GET https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json "HTTP/1.1 200 OK"
2026-10-11 21:17:36,534 - httpx - INFO - HTTP Request: GET https://carnegieendowment.org/rss/solr.xml "HTTP/1.1 404 Not Found"
2026-10-11 21:17:37,214 - httpx - INFO - HTTP Request: GET https://feeds.a.dj.com/rss/RSSMarketsMain.xml "HTTP/1.1 200 OK"
2026-10-11 21:17:37,219 - httpx - INFO - HTTP Request: GET https://www.rand.org/blog.xml "HTTP/1.1 301 Moved Permanently"
2026-10-11 21:17:37,222 - httpx - INFO - HTTP Request: GET https://www.defenseone.com/rss/all/ "HTTP/1.1 200 OK"
2026-10-11 21:17:37,223 - httpx - INFO - HTTP Request: GET https://outbreaknewstoday.com/feed/ "HTTP/1.1 200 OK"
2026-10-11 21:17:37,309 - httpx - INFO - HTTP Request: GET https://www.nature.com/nature.rss "HTTP/1.1 200 OK"
2026-10-11 21:17:37,543 - httpx - INFO - HTTP Request: GET https://www.rand.org/pubs/commentary.xml "HTTP/1.1 200 OK"
2026-10-11 21:17:37,741 - httpx - INFO - HTTP Request: GET https://ucdpapi.pcr.uu.se/api/gedevents/25.1?pagesize=100&page=0 "HTTP/1.1 401 Unauthorized"
2026-10-11 21:17:37,744 - httpx - INFO - HTTP Request: GET https://carnegieendowment.org/rss/solr.xml "HTTP/1.1 404 Not Found"
2026-10-11 21:17:37,960 - httpx - INFO - HTTP Request: GET https://www.timesofisrael.com/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:38,019 - httpx - INFO - HTTP Request: GET https://www.thenationalnews.com/arc/outboundfeeds/rss/?outputType=xml "HTTP/1.1 200 OK"
2026-10-11 21:17:38,043 - httpx - INFO - HTTP Request: GET https://www.iranintl.com/en/feed "HTTP/1.1 200 OK"
2026-10-11 21:17:38,192 - httpx - INFO - HTTP Request: GET https://news.usni.org/feed "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:38,696 - httpx - INFO - HTTP Request: GET https://www.newscientist.com/feed/home/ "HTTP/1.1 301 Moved Permanently"
2026-10-11 21:17:38,699 - httpx - INFO - HTTP Request: GET https://www.militarytimes.com/arc/outboundfeeds/rss/?outputType=xml "HTTP/1.1 200 OK"
2026-10-11 21:17:39,535 - httpx - INFO - HTTP Request: GET https://allafrica.com/tools/headlines/rdf/latest/headlines.rdf "HTTP/1.1 200 OK"
2026-10-11 21:17:39,704 - httpx - INFO - HTTP Request: GET https://www.theafricareport.com/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:39,770 - httpx - INFO - HTTP Request: GET https://www.timesofisrael.com/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:39,923 - httpx - INFO - HTTP Request: GET https://carnegieendowment.org/rss/solr.xml "HTTP/1.1 404 Not Found"
2026-10-11 21:17:39,925 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:carnegie: Client error '404 Not Found' for url 'https://carnegieendowment.org/rss/solr.xml'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
2026-10-11 21:17:40,141 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:scientific_american: 
2026-10-11 21:17:40,181 - httpx - INFO - HTTP Request: GET https://www.newscientist.com/feed/ "HTTP/1.1 200 OK"
2026-10-11 21:17:40,241 - httpx - INFO - HTTP Request: GET https://ucdpapi.pcr.uu.se/api/gedevents/25.1?pagesize=100&page=0 "HTTP/1.1 401 Unauthorized"
2026-10-11 21:17:40,244 - world-intel-mcp.fetcher - WARNING - Fetch failed for ucdp: Client error '401 Unauthorized' for url 'https://ucdpapi.pcr.uu.se/api/gedevents/25.1?pagesize=100&page=0'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401 (url=https://ucdpapi.pcr.uu.se/api/gedevents/25.1)
2026-10-11 21:17:40,244 - world-intel-mcp.sources.conflict - WARNING - UCDP GED API returned no data
2026-10-11 21:17:40,386 - httpx - INFO - HTTP Request: GET https://urlhaus-api.abuse.ch/v1/urls/recent/limit/25/ "HTTP/1.1 401 Unauthorized"
2026-10-11 21:17:40,388 - httpx - INFO - HTTP Request: GET https://africanarguments.org/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:40,390 - world-intel-mcp.fetcher - WARNING - Fetch failed for urlhaus: Client error '401 Unauthorized' for url 'https://urlhaus-api.abuse.ch/v1/urls/recent/limit/25/'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401 (url=https://urlhaus-api.abuse.ch/v1/urls/recent/limit/25/)
2026-10-11 21:17:40,392 - world-intel-mcp.sources.cyber - WARNING - URLhaus feed returned no data
2026-10-11 21:17:41,411 - httpx - INFO - HTTP Request: GET https://www.theafricareport.com/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:41,668 - httpx - INFO - HTTP Request: GET https://africanarguments.org/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:42,843 - httpx - INFO - HTTP Request: GET https://www.timesofisrael.com/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:42,846 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:times_of_israel: Client error '403 Forbidden' for url 'https://www.timesofisrael.com/feed/'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
2026-10-11 21:17:43,562 - world-intel-mcp.vector-store - WARNING - Vector store write failed: [WinError 10061] ����Ŀ�����������ܾ����޷����ӡ�
2026-10-11 21:17:43,939 - httpx - INFO - HTTP Request: GET https://news.usni.org/feed "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:43,940 - httpx - INFO - HTTP Request: GET https://africanarguments.org/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:43,943 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:usni_news: Client error '403 Forbidden' for url 'https://news.usni.org/feed'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
2026-10-11 21:17:43,946 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:african_arguments: Client error '403 Forbidden' for url 'https://africanarguments.org/feed/'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
2026-10-11 21:17:44,039 - httpx - INFO - HTTP Request: GET https://www.theafricareport.com/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:44,041 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:the_africa_report: Client error '403 Forbidden' for url 'https://www.theafricareport.com/feed/'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
2026-10-11 21:17:47,952 - httpx - INFO - HTTP Request: GET https://mexiconewsdaily.com/feed/ "HTTP/1.1 200 OK"
2026-10-11 21:17:47,956 - httpx - INFO - HTTP Request: GET https://www.utilitydive.com/feeds/news/ "HTTP/1.1 200 OK"
2026-10-11 21:17:48,776 - httpx - INFO - HTTP Request: GET https://cleantechnica.com/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:48,830 - httpx - INFO - HTTP Request: GET https://www.carbonbrief.org/feed/ "HTTP/1.1 301 Moved Permanently"
2026-10-11 21:17:49,006 - httpx - INFO - HTTP Request: GET https://oilprice.com/rss/main "HTTP/1.1 200 OK"
2026-10-11 21:17:49,055 - httpx - INFO - HTTP Request: GET https://www.france24.com/fr/rss "HTTP/1.1 200 OK"
2026-10-11 21:17:49,108 - httpx - INFO - HTTP Request: GET https://www.rigzone.com/news/rss/rigzone_latest.aspx "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:49,502 - httpx - INFO - HTTP Request: GET https://www.carbonbrief.org/feed "HTTP/1.1 200 OK"
2026-10-11 21:17:49,553 - httpx - INFO - HTTP Request: GET https://issafrica.org/iss-today/feed "HTTP/1.1 200 OK"
2026-10-11 21:17:49,828 - httpx - INFO - HTTP Request: GET https://www.defense.gov/DesktopModules/ArticleCS/RSS.ashx?ContentType=1&Site=945&max=10 "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:49,958 - httpx - INFO - HTTP Request: GET https://www.state.gov/rss-feed/press-releases/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:50,304 - httpx - INFO - HTTP Request: GET https://www.whitehouse.gov/feed/ "HTTP/1.1 404 Not Found"
2026-10-11 21:17:50,367 - httpx - INFO - HTTP Request: GET https://www.rigzone.com/news/rss/rigzone_latest.aspx "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:50,612 - httpx - INFO - HTTP Request: GET https://reliefweb.int/updates/rss.xml "HTTP/1.1 202 Accepted"
2026-10-11 21:17:50,771 - httpx - INFO - HTTP Request: GET https://www.crisisgroup.org/rss.xml "HTTP/1.1 200 OK"
2026-10-11 21:17:51,102 - httpx - INFO - HTTP Request: GET https://www.americasquarterly.org/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:51,393 - httpx - INFO - HTTP Request: GET https://www.euractiv.com/feed/ "HTTP/1.1 302 Found"
2026-10-11 21:17:51,481 - httpx - INFO - HTTP Request: GET https://www.whitehouse.gov/feed/ "HTTP/1.1 404 Not Found"
2026-10-11 21:17:51,551 - httpx - INFO - HTTP Request: GET https://cleantechnica.com/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:51,767 - httpx - INFO - HTTP Request: GET https://www.defense.gov/DesktopModules/ArticleCS/RSS.ashx?ContentType=1&Site=945&max=10 "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:51,840 - httpx - INFO - HTTP Request: GET https://dialogo-americas.com/feed/ "HTTP/1.1 200 OK"
2026-10-11 21:17:52,439 - httpx - INFO - HTTP Request: GET https://www.rapporteur.com/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:52,683 - httpx - INFO - HTTP Request: GET https://www.rigzone.com/news/rss/rigzone_latest.aspx "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:52,684 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:rigzone: Client error '403 Forbidden' for url 'https://www.rigzone.com/news/rss/rigzone_latest.aspx'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
2026-10-11 21:17:52,981 - httpx - INFO - HTTP Request: GET https://www.batimes.com.ar/feed "HTTP/1.1 200 OK"
2026-10-11 21:17:53,659 - httpx - INFO - HTTP Request: GET https://www.dawn.com/feeds/home "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:53,663 - httpx - INFO - HTTP Request: GET https://www.who.int/rss-feeds/news-english.xml "HTTP/1.1 200 OK"
2026-10-11 21:17:53,689 - httpx - INFO - HTTP Request: GET https://ticotimes.net/feed "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:53,691 - httpx - INFO - HTTP Request: GET https://www.statnews.com/feed/ "HTTP/1.1 200 OK"
2026-10-11 21:17:53,772 - httpx - INFO - HTTP Request: GET https://www.whitehouse.gov/feed/ "HTTP/1.1 404 Not Found"
2026-10-11 21:17:53,794 - httpx - INFO - HTTP Request: GET https://scroll.in/feed "HTTP/1.1 308 Permanent Redirect"
2026-10-11 21:17:54,047 - httpx - INFO - HTTP Request: GET https://insightcrime.org/feed/ "HTTP/1.1 200 OK"
2026-10-11 21:17:54,106 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:white_house: Client error '404 Not Found' for url 'https://www.whitehouse.gov/feed/'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
2026-10-11 21:17:54,134 - httpx - INFO - HTTP Request: GET https://cleantechnica.com/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:54,137 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:cleantechnica: Client error '403 Forbidden' for url 'https://cleantechnica.com/feed/'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
2026-10-11 21:17:54,294 - httpx - INFO - HTTP Request: GET https://www.defense.gov/DesktopModules/ArticleCS/RSS.ashx?ContentType=1&Site=945&max=10 "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:54,296 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:dod_news: Client error '403 Forbidden' for url 'https://www.defense.gov/DesktopModules/ArticleCS/RSS.ashx?ContentType=1&Site=945&max=10'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
2026-10-11 21:17:54,309 - httpx - INFO - HTTP Request: GET https://www.euractiv.com/feed/ "HTTP/1.1 302 Found"
2026-10-11 21:17:54,397 - httpx - INFO - HTTP Request: GET https://scroll.in/feed/ "HTTP/1.1 301 Moved Permanently"
2026-10-11 21:17:54,627 - httpx - INFO - HTTP Request: GET https://euobserver.com/rss "HTTP/1.1 301 "
2026-10-11 21:17:54,679 - httpx - INFO - HTTP Request: GET https://www.thelancet.com/rssfeed/lancet_current.xml "HTTP/1.1 200 OK"
2026-10-11 21:17:54,887 - httpx - INFO - HTTP Request: GET https://scroll.in/page/1 "HTTP/1.1 200 OK"
2026-10-11 21:17:54,889 - httpx - INFO - HTTP Request: GET https://www.rapporteur.com/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:54,890 - httpx - INFO - HTTP Request: GET https://medicalxpress.com/rss-feed/ "HTTP/1.1 200 OK"
2026-10-11 21:17:54,985 - httpx - INFO - HTTP Request: GET https://brazilian.report/feed/ "HTTP/1.1 404 Not Found"
2026-10-11 21:17:55,203 - httpx - INFO - HTTP Request: GET https://euobserver.com/feed/ "HTTP/1.1 200 "
2026-10-11 21:17:55,316 - httpx - INFO - HTTP Request: GET https://astanatimes.com/feed/ "HTTP/1.1 200 OK"
2026-10-11 21:17:55,484 - httpx - INFO - HTTP Request: GET https://www.state.gov/rss-feed/press-releases/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:55,868 - httpx - INFO - HTTP Request: GET https://ticotimes.net/feed "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:55,870 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:tico_times: Client error '403 Forbidden' for url 'https://ticotimes.net/feed'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
2026-10-11 21:17:56,055 - httpx - INFO - HTTP Request: GET https://www.highnorthnews.com/en/rss.xml "HTTP/1.1 200 OK"
2026-10-11 21:17:56,198 - httpx - INFO - HTTP Request: GET https://thebarentsobserver.com/en/rss.xml "HTTP/1.1 301 Moved Permanently"
2026-10-11 21:17:56,205 - httpx - INFO - HTTP Request: GET https://gcaptain.com/feed/ "HTTP/1.1 200 OK"
2026-10-11 21:17:56,486 - httpx - INFO - HTTP Request: GET https://www.dawn.com/feeds/home "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:56,678 - httpx - INFO - HTTP Request: GET https://lloydslist.maritimeintelligence.informa.com/rss/all "HTTP/1.1 301 Moved Permanently"
2026-10-11 21:17:56,760 - httpx - INFO - HTTP Request: GET https://www.nasaspaceflight.com/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:56,901 - httpx - INFO - HTTP Request: GET https://www.arctictoday.com/feed/ "HTTP/1.1 301 Moved Permanently"
2026-10-11 21:17:57,077 - httpx - INFO - HTTP Request: GET https://spaceref.com/feed/ "HTTP/1.1 301 Moved Permanently"
2026-10-11 21:17:57,129 - httpx - INFO - HTTP Request: GET https://www.arctictoday.com "HTTP/1.1 200 OK"
2026-10-11 21:17:57,211 - httpx - INFO - HTTP Request: GET https://www.space.com/feeds/all "HTTP/1.1 301 Moved Permanently"
2026-10-11 21:17:57,314 - httpx - INFO - HTTP Request: GET https://www.thebarentsobserver.com/en/rss.xml "HTTP/1.1 200 OK"
2026-10-11 21:17:57,484 - httpx - INFO - HTTP Request: GET https://lloydslist.com/rss/all "HTTP/1.1 301 Moved Permanently"
2026-10-11 21:17:57,604 - httpx - INFO - HTTP Request: GET http://www.space.com/feeds.xml "HTTP/1.1 301 Moved Permanently"
2026-10-11 21:17:57,788 - httpx - INFO - HTTP Request: GET https://www.space.com/feeds.xml "HTTP/1.1 200 OK"
2026-10-11 21:17:58,170 - httpx - INFO - HTTP Request: GET https://www.euractiv.com/feed/ "HTTP/1.1 302 Found"
2026-10-11 21:17:58,529 - httpx - INFO - HTTP Request: GET https://www.nasaspaceflight.com/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:58,758 - httpx - INFO - HTTP Request: GET https://www.lloydslist.com/rss/all "HTTP/1.1 200 OK"
2026-10-11 21:17:58,816 - httpx - INFO - HTTP Request: GET https://www.nti.org/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:58,822 - httpx - INFO - HTTP Request: GET https://world-nuclear-news.org/rss "HTTP/1.1 200 OK"
2026-10-11 21:17:59,078 - httpx - INFO - HTTP Request: GET https://www.spaceref.com/feed/ "HTTP/1.1 410 Gone"
2026-10-11 21:17:59,431 - httpx - INFO - HTTP Request: GET https://www.rapporteur.com/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:59,434 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:euractiv: Client error '403 Forbidden' for url 'https://www.rapporteur.com/feed/'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
2026-10-11 21:17:59,628 - httpx - INFO - HTTP Request: GET https://www.dawn.com/feeds/home "HTTP/1.1 403 Forbidden"
2026-10-11 21:17:59,630 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:dawn_pakistan: Client error '403 Forbidden' for url 'https://www.dawn.com/feeds/home'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
2026-10-11 21:17:59,780 - httpx - INFO - HTTP Request: GET https://www.armscontrol.org/rss/all "HTTP/1.1 404 Not Found"
2026-10-11 21:17:59,978 - httpx - INFO - HTTP Request: GET https://www.eenews.net/feed/ "HTTP/1.1 200 OK"
2026-10-11 21:18:00,340 - httpx - INFO - HTTP Request: GET https://insideclimatenews.org/feed/ "HTTP/1.1 200 OK"
2026-10-11 21:18:00,393 - httpx - INFO - HTTP Request: GET https://spaceref.com/feed/ "HTTP/1.1 301 Moved Permanently"
2026-10-11 21:18:00,755 - httpx - INFO - HTTP Request: GET https://www.spaceref.com/feed/ "HTTP/1.1 410 Gone"
2026-10-11 21:18:01,113 - httpx - INFO - HTTP Request: GET https://www.nasaspaceflight.com/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:18:01,116 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:nasaspaceflight: Client error '403 Forbidden' for url 'https://www.nasaspaceflight.com/feed/'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
2026-10-11 21:18:01,190 - httpx - INFO - HTTP Request: GET https://www.climatechangenews.com/feed/ "HTTP/1.1 200 OK"
2026-10-11 21:18:01,414 - httpx - INFO - HTTP Request: GET https://www.nti.org/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:18:01,557 - httpx - INFO - HTTP Request: GET https://www.armscontrol.org/rss/all "HTTP/1.1 404 Not Found"
2026-10-11 21:18:03,167 - httpx - INFO - HTTP Request: GET https://spaceref.com/feed/ "HTTP/1.1 301 Moved Permanently"
2026-10-11 21:18:03,551 - httpx - INFO - HTTP Request: GET https://www.spaceref.com/feed/ "HTTP/1.1 410 Gone"
2026-10-11 21:18:03,552 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:spaceref: Client error '410 Gone' for url 'https://www.spaceref.com/feed/'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/410
2026-10-11 21:18:04,158 - httpx - INFO - HTTP Request: GET https://www.armscontrol.org/rss/all "HTTP/1.1 404 Not Found"
2026-10-11 21:18:04,351 - httpx - INFO - HTTP Request: GET https://www.nti.org/feed/ "HTTP/1.1 403 Forbidden"
2026-10-11 21:18:04,354 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:nuclear_threat_initiative: Client error '403 Forbidden' for url 'https://www.nti.org/feed/'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403
2026-10-11 21:18:04,606 - world-intel-mcp.fetcher - WARNING - Text fetch failed for rss:arms_control_assn: Client error '404 Not Found' for url 'https://www.armscontrol.org/rss/all'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
2026-10-11 21:18:15,381 - mcp.server.lowlevel.server - INFO - Warning: UserWarning: Failed to obtain server version. Unable to check client-server compatibility. Set check_compatibility=False to skip version check.

==================================================
🎉 成功调用 MCP 工具！返回的真实数据如下：
==================================================
{
  "markdown": "# Daily Intelligence Digest (2026-10-11)\n\n## Top Events by Domain\n- **Earthquakes** [1]: M5.3 earthquake, southeast of Easter Island\n- **Military** [2]: 53 military aircraft currently tracked\n- **Cyber** [3]: QakBot, 50.16.16.211 (critical severity)\n- **Space Weather** [4]: Kp index 3.0\n- **Health** [5]: Sustained heat raises infectious disease risks across Europe, ECDC warns\n- **Aviation** [11]: 9559 aircraft airborne globally\n\n## Headlines\n- [6] Brazil's Lula accuses social media giant Meta of election interference amid tight run-off campaign (https://www.france24.com/en/americas/20261011-brazil-lula-accuses-social-media-giant-meta-election-interference-amid-tight-run-campaign)\n- [7] New algorithm could predict Arctic sea ice up to 9 months ahead, offering new climate insights (https://phys.org/news/2026-10-algorithm-arctic-sea-ice-months.html)\n- [8] Sudan: Diplomatic Setbacks Undermine U.S. Approach to Sudan (https://allafrica.com/stories/202610110093.html)\n- [9] Abu Dhabi plans major road upgrades in Mussaffah to ease congestion and improve links (https://www.thenationalnews.com/news/uae/2026/10/11/abu-dhabi-plans-major-road-upgrades-in-mussaffah-to-ease-congestion-and-improve-links/)\n- [10] RTA wins Dubai-it Award for delivering projects at record speed (https://www.thenationalnews.com/news/uae/2026/10/11/rta-wins-dubai-it-award-for-delivering-projects-at-record-speed/)\n\n## Trends (6h vs. 48h baseline)\n_Unavailable: [WinError 10061] \u7531\u4e8e\u76ee\u6807\u8ba1\u7b97\u673a\u79ef\u6781\u62d2\u7edd\uff0c\u65e0\u6cd5\u8fde\u63a5\u3002._\n\n## Timeline (last 24h)\n_Unavailable: [WinError 10061] \u7531\u4e8e\u76ee\u6807\u8ba1\u7b97\u673a\u79ef\u6781\u62d2\u7edd\uff0c\u65e0\u6cd5\u8fde\u63a5\u3002._\n\n## Data Gaps\n- Wildfires: NASA_FIRMS_API_KEY not configured\n- Traffic: TOMTOM_API_KEY not configured\n- trend detection unavailable: [WinError 10061] \u7531\u4e8e\u76ee\u6807\u8ba1\u7b97\u673a\u79ef\u6781\u62d2\u7edd\uff0c\u65e0\u6cd5\u8fde\u63a5\u3002\n- timeline unavailable: [WinError 10061] \u7531\u4e8e\u76ee\u6807\u8ba1\u7b97\u673a\u79ef\u6781\u62d2\u7edd\uff0c\u65e0\u6cd5\u8fde\u63a5\u3002",
  "sources": [
    {
      "n": 1,
      "domain": "earthquakes",
      "description": "M5.3 earthquake, southeast of Easter Island",
      "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000u1gs",
      "timestamp": "2026-10-10T21:34:02Z"
    },
    {
      "n": 2,
      "domain": "military",
      "description": "53 military aircraft currently tracked",
      "timestamp": "2026-10-11T13:17:36.150782+00:00"
    },
    {
      "n": 3,
      "domain": "cyber",
      "description": "QakBot, 50.16.16.211 (critical severity)",
      "timestamp": "2025-12-30 13:56:31"
    },
    {
      "n": 4,
      "domain": "space_weather",
      "description": "Kp index 3.0",
      "timestamp": "2026-10-11T13:17:36.535726+00:00"
    },
    {
      "n": 5,
      "domain": "health",
      "description": "Sustained heat raises infectious disease risks across Europe, ECDC warns",
      "url": "https://outbreaknewstoday.com/sustained-heat-raises-infectious-disease-risks-across-europe-ecdc-warns-741/?utm_source=rss&utm_medium=rss&utm_campaign=sustained-heat-raises-infectious-disease-risks-across-europe-ecdc-warns",
      "timestamp": "2026-07-30T00:08:22Z"
    },
    {
      "n": 6,
      "domain": "news",
      "description": "Brazil's Lula accuses social media giant Meta of election interference amid tight run-off campaign",
      "url": "https://www.france24.com/en/americas/20261011-brazil-lula-accuses-social-media-giant-meta-election-interference-amid-tight-run-campaign",
      "timestamp": "2026-10-11T05:12:09Z"
    },
    {
      "n": 7,
      "domain": "news",
      "description": "New algorithm could predict Arctic sea ice up to 9 months ahead, offering new climate insights",
      "url": "https://phys.org/news/2026-10-algorithm-arctic-sea-ice-months.html",
      "timestamp": "2026-10-11T05:00:01Z"
    },
    {
      "n": 8,
      "domain": "news",
      "description": "Sudan: Diplomatic Setbacks Undermine U.S. Approach to Sudan",
      "url": "https://allafrica.com/stories/202610110093.html",
      "timestamp": "2026-10-11T04:50:09Z"
    },
    {
      "n": 9,
      "domain": "news",
      "description": "Abu Dhabi plans major road upgrades in Mussaffah to ease congestion and improve links",
      "url": "https://www.thenationalnews.com/news/uae/2026/10/11/abu-dhabi-plans-major-road-upgrades-in-mussaffah-to-ease-congestion-and-improve-links/",
      "timestamp": "2026-10-11T04:49:04Z"
    },
    {
      "n": 10,
      "domain": "news",
      "description": "RTA wins Dubai-it Award for delivering projects at record speed",
      "url": "https://www.thenationalnews.com/news/uae/2026/10/11/rta-wins-dubai-it-award-for-delivering-projects-at-record-speed/",
      "timestamp": "2026-10-11T04:48:29Z"
    },
    {
      "n": 11,
      "domain": "aviation",
      "description": "9559 aircraft airborne globally",
      "timestamp": "2026-10-11T13:17:38Z"
    }
  ],
  "cited": true,
  "data_gaps": [
    "Wildfires: NASA_FIRMS_API_KEY not configured",
    "Traffic: TOMTOM_API_KEY not configured",
    "trend detection unavailable: [WinError 10061] \u7531\u4e8e\u76ee\u6807\u8ba1\u7b97\u673a\u79ef\u6781\u62d2\u7edd\uff0c\u65e0\u6cd5\u8fde\u63a5\u3002",
    "timeline unavailable: [WinError 10061] \u7531\u4e8e\u76ee\u6807\u8ba1\u7b97\u673a\u79ef\u6781\u62d2\u7edd\uff0c\u65e0\u6cd5\u8fde\u63a5\u3002"
  ],
  "vector_store_available": true,
  "source": "daily-digest",
  "timestamp": "2026-10-11T13:17:23.164637+00:00"
}

进程已结束，退出代码为 0

附录（示例图）
![[PixPin_2026-10-11_21-35-32 1.png]]
![[PixPin_2026-10-11_21-38-05.png]]