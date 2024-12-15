from requests import get
from random import choice
LISTAHAN = [
    "https://vt.tiktok.com/ZSYwJj3J1/",
    "https://vt.tiktok.com/ZS2foDweF/",
    "https://vt.tiktok.com/ZS2fo5yFA/",
    "https://vt.tiktok.com/ZSY9eoqp9/",
    "https://vt.tiktok.com/ZS2oCYhTP/",
    "https://vt.tiktok.com/ZS2foUQVL/",
    "https://vt.tiktok.com/ZS214wFbB/",
    "https://vt.tiktok.com/ZS2foSwnX/",
    "https://www.tiktok.com/@leiangeleecruz613/video/7393996938212805906?_r=1&amp;u_code=e275f59dg9eiib&amp;region=PH&amp;mid=7370521417198488325&amp;preview_pb=0&amp;sharer_language=en&amp;_d=dl4ad62m31bah3&amp;share_item_id=7393996938212805906&amp;source=h5_t&amp;timestamp=1722981314&amp;user_id=7107242558354474010&amp;sec_user_id=MS4wLjABAAAA-cPSGip-M0kC_JB4WQt8XGxH4I0mgTbqqDO4ANoTrWwdgHh9GDU7PzvKZgYgfQq1&amp;social_share_type=0&amp;utm_source=copy&amp;utm_campaign=client_share&amp;utm_medium=android&amp;share_iid=7355345020910634758&amp;share_link_id=69323fd2-03f0-4d78-ac24-a06de3a34d34&amp;share_app_id=1180&amp;ugbiz_name=MAIN&amp;ug_btm=b8727%2Cb2878&amp;enable_checksum=1",
    "https://vt.tiktok.com/ZSYmyMhTR/",
    "https://vt.tiktok.com/ZSYckFUph/",
    "https://vt.tiktok.com/ZSYwJLJxf/",
    "https://vt.tiktok.com/ZS21V6htd/",
    "https://vt.tiktok.com/ZSYwJA4yY/",
    "https://vt.tiktok.com/ZSYjFsBaa/",
    "https://vt.tiktok.com/ZS214EEBS/",
    "https://vt.tiktok.com/ZS2foSa1B/",
    "https://vt.tiktok.com/ZSYwJfjut/",
    "https://vt.tiktok.com/ZS214cbjU/",
    "https://vt.tiktok.com/ZSYwJMrS9/",
    "https://vt.tiktok.com/ZS21VY25h/",
    "https://vt.tiktok.com/ZSYwJ2B19/",
    "https://vt.tiktok.com/ZS21V2xTK/",
    "https://www.tiktok.com/@xopianne/video/7377434726111431942?q=beautifulgirl",
    "https://vt.tiktok.com/ZSYwJSp7t/",
    "https://vt.tiktok.com/ZS2foaURk/",
    "https://vt.tiktok.com/ZS2o7ApXE/",
    "https://vt.tiktok.com/ZSYck2XGV/",
    "https://vt.tiktok.com/ZSYwJyHQ9/",
    "https://www.tiktok.com/@leiangeleecruz613/video/7385477283223489808?_r=1&amp;u_code=e275f59dg9eiib&amp;region=PH&amp;mid=7382658258613373712&amp;preview_pb=0&amp;sharer_language=en&amp;_d=dl4ad62m31bah3&amp;share_item_id=7385477283223489808&amp;source=h5_t&amp;timestamp=1722981302&amp;user_id=7107242558354474010&amp;sec_user_id=MS4wLjABAAAA-cPSGip-M0kC_JB4WQt8XGxH4I0mgTbqqDO4ANoTrWwdgHh9GDU7PzvKZgYgfQq1&amp;social_share_type=0&amp;utm_source=copy&amp;utm_campaign=client_share&amp;utm_medium=android&amp;share_iid=7355345020910634758&amp;share_link_id=7ffb634f-88d0-40d1-bb54-bebfdfc3ebe2&amp;share_app_id=1180&amp;ugbiz_name=MAIN&amp;ug_btm=b8727%2Cb2878&amp;enable_checksum=1",
    "https://vt.tiktok.com/ZSY9eTDY2/",
    "https://vt.tiktok.com/ZSYmyRw9g/",
    "https://vt.tiktok.com/ZSYwJLbG8/",
    "https://vt.tiktok.com/ZSYwJS4To/",
    "https://vt.tiktok.com/ZSYckY9dF/",
    "https://vt.tiktok.com/ZSYyyQegM/",
    "https://vt.tiktok.com/ZSYckUH8f/",
    "https://vt.tiktok.com/ZSY9e7kYR/",
    "https://vt.tiktok.com/ZSYck55L1/",
    "https://vt.tiktok.com/ZS2foBNoP/",
    "https://vt.tiktok.com/ZSYwJ5L9D/",
    "https://vt.tiktok.com/ZS21Vrjy5/",
    "https://vt.tiktok.com/ZSYckueBf/",
    "https://vt.tiktok.com/ZSYwJMSj3/",
    "https://vt.tiktok.com/ZS21VLc7K/",
    "https://vt.tiktok.com/ZSYckS4gF/",
    "https://vt.tiktok.com/ZS2foh11P/",
    "https://vt.tiktok.com/ZSYyyHeQN/",
    "https://vt.tiktok.com/ZS214vUWm/",
    "https://vt.tiktok.com/ZSYwJ6aa4/",
    "https://vt.tiktok.com/ZSYjYdye7/",
    "https://vt.tiktok.com/ZS21VJRL9/",
    "https://vt.tiktok.com/ZSYV2Y63f/",
    "https://vt.tiktok.com/ZSYV226hS/",
    "https://vt.tiktok.com/ZS214vMJK/",
    "https://vt.tiktok.com/ZS2fo4MQ8/",
    "https://vt.tiktok.com/ZSY9etwRd/",
    "https://vt.tiktok.com/ZSYwJPWTD/",
    "https://vt.tiktok.com/ZSYwJrVHR/",
    "https://vt.tiktok.com/ZS2foDm7p/",
    "https://vt.tiktok.com/ZS2fogFcy/",
    "https://vt.tiktok.com/ZSYwJkDbH/",
    "https://vt.tiktok.com/ZSYckkGWv/",
    "https://vt.tiktok.com/ZS21VjG22/",
    "https://vt.tiktok.com/ZSYwJdhDM/",
    "https://vt.tiktok.com/ZSYck6Yfk/",
    "https://vt.tiktok.com/ZS2fo5FgU/",
    "https://vt.tiktok.com/ZSYwJfosg/",
    "https://vt.tiktok.com/ZSYckrPkF/",
    "https://vt.tiktok.com/ZS2foa3rV/",
    "https://vt.tiktok.com/ZS2fohqjK/",
    "https://vt.tiktok.com/ZSYwJBpht/",
    "https://vt.tiktok.com/ZSYwJN6tw/",
    "https://vt.tiktok.com/ZSYwJPHAB/",
    "https://vt.tiktok.com/ZS21VMfmJ/",
    "https://vt.tiktok.com/ZSYJLAp8e/",
    "https://vt.tiktok.com/ZSYwJSvWd/",
    "https://vt.tiktok.com/ZS21VF6xG/",
    "https://vt.tiktok.com/ZSYmyJs3J/",
    "https://vt.tiktok.com/ZS2foP4uQ/",
    "https://vt.tiktok.com/ZS2oXxPYP/",
    "https://vt.tiktok.com/ZSYckPsCu/",
    "https://vt.tiktok.com/ZSYyyGfrU/",
    "https://vt.tiktok.com/ZSYPsVKvS/",
    "https://vt.tiktok.com/ZS214ojrH/",
    "https://www.tiktok.com/@leiangeleecruz613/video/7393996938212805906?_r=1&amp;u_code=e275f59dg9eiib&amp;region=PH&amp;mid=7370521417198488325&amp;preview_pb=0&amp;sharer_language=en&amp;_d=dl4ad62m31bah3&amp;share_item_id=7393996938212805906&amp;source=h5_t&amp;timestamp=1722981323&amp;user_id=7107242558354474010&amp;sec_user_id=MS4wLjABAAAA-cPSGip-M0kC_JB4WQt8XGxH4I0mgTbqqDO4ANoTrWwdgHh9GDU7PzvKZgYgfQq1&amp;social_share_type=0&amp;utm_source=copy&amp;utm_campaign=client_share&amp;utm_medium=android&amp;share_iid=7355345020910634758&amp;share_link_id=8e107080-0767-4e1b-96da-04ed1c5d7370&amp;share_app_id=1180&amp;ugbiz_name=MAIN&amp;ug_btm=b8727%2Cb2878&amp;enable_checksum=1iew_pb=0&amp;sharer_language=en&amp;_d=dl4ad62m31bah3&amp;share_item_id=7379173272069393665&amp;source=h5_t&amp;timestamp=1722981326&amp;user_id=7107242558354474010&amp;sec_user_id=MS4wLjABAAAA-cPSGip-M0kC_JB4WQt8XGxH4I0mgTbqqDO4ANoTrWwdgHh9GDU7PzvKZgYgfQq1&amp;social_share_type=0&amp;utm_source=copy&amp;utm_campaign=client_share&amp;utm_medium=android&amp;share_iid=7355345020910634758&amp;share_link_id=6664c40a-1928-4ef2-80ae-c22adba6a7f6&amp;share_app_id=1180&amp;ugbiz_name=MAIN&amp;ug_btm=b8727%2Cb2878&amp;enable_checksum=1",
    "https://vt.tiktok.com/ZS2oX9RUN/",
    "https://vt.tiktok.com/ZS2fomVMC/",
    "https://vt.tiktok.com/ZS2fogqkg/",
    "https://vt.tiktok.com/ZSYwJ1SqQ/",
    "https://vt.tiktok.com/ZSYwJFfw5/",
    "https://www.tiktok.com/@leiangeleecruz613/video/7393996938212805906?_r=1&amp;u_code=e275f59dg9eiib&amp;region=PH&amp;mid=7370521417198488325&amp;preview_pb=0&amp;sharer_language=en&amp;_d=dl4ad62m31bah3&amp;share_item_id=7393996938212805906&amp;source=h5_t&amp;timestamp=1722981317&amp;user_id=7107242558354474010&amp;sec_user_id=MS4wLjABAAAA-cPSGip-M0kC_JB4WQt8XGxH4I0mgTbqqDO4ANoTrWwdgHh9GDU7PzvKZgYgfQq1&amp;social_share_type=0&amp;utm_source=copy&amp;utm_campaign=client_share&amp;utm_medium=android&amp;share_iid=7355345020910634758&amp;share_link_id=eea48c99-1aed-40d9-ac00-0be7b1ad07a8&amp;share_app_id=1180&amp;ugbiz_name=MAIN&amp;ug_btm=b8727%2Cb2878&amp;enable_checksum=1",
    "https://vt.tiktok.com/ZSYjFt1j7/",
    "https://vt.tiktok.com/ZS2fombkG/",
    "https://vt.tiktok.com/ZS214vpJs/",
    "https://vt.tiktok.com/ZSY9e73Mh/",
    "https://vt.tiktok.com/ZS21VMG1r/",
    "https://www.tiktok.com/@chelsixxi/video/7268691248754511109?is_from_webapp=1",
    "https://vt.tiktok.com/ZS2foBuSG/",
    "https://vt.tiktok.com/ZSYckNJeG/",
    "https://vt.tiktok.com/ZSYckLUq1/",
    "https://vt.tiktok.com/ZS21VdSFK/",
    "https://vt.tiktok.com/ZS2foakxk/",
    "https://vt.tiktok.com/ZS2foHfKA/",
    "https://vt.tiktok.com/ZS214KY9a/",
    "https://vt.tiktok.com/ZSYwJLybH/",
    "https://vt.tiktok.com/ZSYwJPpDY/",
    "https://vt.tiktok.com/ZSYwJk7w1/",
    "https://www.tiktok.com/@fil.spotted14/video/7369284882926816518?is_from_webapp=1",
    "https://vt.tiktok.com/ZS21VdhGo/",
    "https://vt.tiktok.com/ZS2foXqD3/",
    "https://vt.tiktok.com/ZS2fou4ru/",
    "https://vt.tiktok.com/ZSYbrHgR3/",
    "https://vt.tiktok.com/ZSYckmhE4/",
    "https://vt.tiktok.com/ZS2foUeDK/",
    "https://vt.tiktok.com/ZSYckjTNT/",
    "https://vt.tiktok.com/ZS21Vk7Ac/",
    "https://vt.tiktok.com/ZS214oLkk/",
    "https://vt.tiktok.com/ZS21V2WhD/",
    "https://vt.tiktok.com/ZS21VJRp1/",
    "https://vt.tiktok.com/ZS214vUVG/",
    "https://vt.tiktok.com/ZSYwJjNR8/",
    "https://vt.tiktok.com/ZSYyyVY9Y/",
    "https://vt.tiktok.com/ZS21VYvtq/",
    "https://vt.tiktok.com/ZS2foqCaN/",
    "https://vt.tiktok.com/ZSYPs5bRy/",
    "https://vt.tiktok.com/ZSYmyBU35/",
    "https://vt.tiktok.com/ZS21VFYhs/",
    "https://vt.tiktok.com/ZSYwJ1wpP/",
    "https://vt.tiktok.com/ZS2foXtu2/",
    "https://vt.tiktok.com/ZS2fo9oGd/",
    "https://vt.tiktok.com/ZSYPsmmXq/",
    "https://vt.tiktok.com/ZSYwJSnwn/",
    "https://vt.tiktok.com/ZSYckYbnY/",
    "https://vt.tiktok.com/ZSYwJ5LFQ/",
    "https://vt.tiktok.com/ZSYckaTjY/",
    "https://vt.tiktok.com/ZS2foxQAe/",
    "https://vt.tiktok.com/ZSY9e7pns/",
    "https://vt.tiktok.com/ZS2fo5rn7/",
    "https://vt.tiktok.com/ZS2fo9Us8/",
    "https://vt.tiktok.com/ZS21VJEu4/",
    "https://vt.tiktok.com/ZS2fomCcf/",
    "https://vt.tiktok.com/ZS214TSxm/",
    "https://vt.tiktok.com/ZS2foynso/",
    "https://vt.tiktok.com/ZS21V2Qex/",
    "https://vt.tiktok.com/ZSYyfdpsp/",
    "https://vt.tiktok.com/ZSYyyb6nL/",
    "https://vt.tiktok.com/ZSYmyYX9q/",
    "https://vt.tiktok.com/ZS21VeLGM/",
    "https://vt.tiktok.com/ZSYbM3Nrx/",
    "https://vt.tiktok.com/ZSYwJeQHX/",
    "https://vt.tiktok.com/ZSYwJkTBu/",
    "https://www.tiktok.com/@acrnzn/video/7357948063505190150?_r=1&amp;u_code=dm5keej0gd9a33&amp;region=PH&amp;mid=7311769526328920837&amp;preview_pb=0&amp;sharer_language=en&amp;_d=e9dff64ach0099&amp;share_item_id=7357948063505190150&amp;source=h5_t&amp;timestamp=1715127419&amp;user_id=7040213398981837851&amp;sec_user_id=MS4wLjABAAAA_aLT9EGUMQF-89KUchhsrj4rqyHpQYMAFazpNsTl3oU_Am8di06k-fDMcseaadmO&amp;social_share_type=0&amp;utm_source=copy&amp;utm_campaign=client_share&amp;utm_medium=android&amp;share_iid=7363816494881441541&amp;share_link_id=89c247a9-1de3-49dc-bd49-08291ed97bb3&amp;share_app_id=1180&amp;ugbiz_name=MAIN&amp;ug_btm=b2001&amp;enable_checksum=1",
    "https://vt.tiktok.com/ZSYwJjC4k/",
    "https://vt.tiktok.com/ZSYmyhBJj/",
    "https://vt.tiktok.com/ZS2forXj6/",
    "https://vt.tiktok.com/ZS2fouHsW/",
    "https://vt.tiktok.com/ZSY9eWYxP/",
    "https://vt.tiktok.com/ZS2foUwBa/",
    "https://vt.tiktok.com/ZS2fo4chS/",
    "https://vt.tiktok.com/ZSYwJF3s8/",
    "https://vt.tiktok.com/ZSYbMEWBK/",
    "https://vt.tiktok.com/ZS21VMqsF/",
    "https://vt.tiktok.com/ZSYyfMrjY/",
    "https://vt.tiktok.com/ZSYmykLR9/",
    "https://vt.tiktok.com/ZSYwJhJPs/",
    "https://vt.tiktok.com/ZSYwJjNoN/",
    "https://vt.tiktok.com/ZSYwJegg3/",
    "https://vt.tiktok.com/ZS21VhaKp/",
    "https://www.tiktok.com/@leiangeleecruz613/video/7393996938212805906?_r=1&amp;u_code=e275f59dg9eiib&amp;region=PH&amp;mid=7370521417198488325&amp;preview_pb=0&amp;sharer_language=en&amp;_d=dl4ad62m31bah3&amp;share_item_id=7393996938212805906&amp;source=h5_t&amp;timestamp=1722981320&amp;user_id=7107242558354474010&amp;sec_user_id=MS4wLjABAAAA-cPSGip-M0kC_JB4WQt8XGxH4I0mgTbqqDO4ANoTrWwdgHh9GDU7PzvKZgYgfQq1&amp;social_share_type=0&amp;utm_source=copy&amp;utm_campaign=client_share&amp;utm_medium=android&amp;share_iid=7355345020910634758&amp;share_link_id=b8670d00-5513-4a92-90c6-a0f24493c8ad&amp;share_app_id=1180&amp;ugbiz_name=MAIN&amp;ug_btm=b8727%2Cb2878&amp;enable_checksum=1",
    "https://vt.tiktok.com/ZSYyfjQqS/",
    "https://vt.tiktok.com/ZS2foDpys/",
    "https://vt.tiktok.com/ZS2fohWa3/",
    "https://vt.tiktok.com/ZS2foy9Cy/",
    "https://vt.tiktok.com/ZS214v9QH/",
    "https://www.tiktok.com/@thannini/video/7333647500085153025?_t=8m4K1SrvnKn&amp;_r=1",
    "https://vt.tiktok.com/ZS2foaA7G/",
    "https://vt.tiktok.com/ZS2fE7BGL/",
    "https://vt.tiktok.com/ZSYckBxoa/",
    "https://vt.tiktok.com/ZS2fo4Ah7/",
    "https://vt.tiktok.com/ZS21VYyDX/",
    "https://vt.tiktok.com/ZSYPs4F71/",
    "https://vt.tiktok.com/ZS21VNFd8/",
    "https://vt.tiktok.com/ZSYwJfnJg/",
    "https://vt.tiktok.com/ZSYwJ1PhX/",
    "https://vt.tiktok.com/ZSYwJfMoE/",
    "https://vt.tiktok.com/ZS214wWhs/",
    "https://vt.tiktok.com/ZS21VLmVb/",
    "https://vt.tiktok.com/ZSYckH7TM/",
    "https://vt.tiktok.com/ZSYbMcts8/",
    "https://vt.tiktok.com/ZS21438o7/",
    "https://vt.tiktok.com/ZSYwJUgPw/",
    "https://vt.tiktok.com/ZSYjFtNxj/",
    "https://vt.tiktok.com/ZSFotUkUx/",
    "https://vt.tiktok.com/ZSYwJeTMu/",
    "https://vt.tiktok.com/ZSYPsUoeR/",
    "https://vt.tiktok.com/ZS2oQvcyE/",
    "https://vt.tiktok.com/ZS21VeLWF/",
    "https://vt.tiktok.com/ZSY9eWkDF/",
    "https://vt.tiktok.com/ZSYwJAp1G/",
    "https://vt.tiktok.com/ZS214EJnF/",
    "https://vt.tiktok.com/ZSYyypBcg/",
    "https://vt.tiktok.com/ZSY9demF8/",
    "https://vt.tiktok.com/ZS2omU961/",
    "https://vt.tiktok.com/ZSYyymQ9M/",
    "https://vt.tiktok.com/ZS2fokRqY/",
    "https://vt.tiktok.com/ZS2foSGxo/",
    "https://vt.tiktok.com/ZSYwJ6N6K/",
    "https://vt.tiktok.com/ZS2oQyeoN/",
    "https://vt.tiktok.com/ZS2foVbFC/",
    "https://vt.tiktok.com/ZS2foUw4V/",
    "https://vt.tiktok.com/ZS2fo5sFj/",
    "https://vt.tiktok.com/ZS2foyMqN/",
    "https://vt.tiktok.com/ZS2fo431m/",
    "https://vt.tiktok.com/ZS21Vr9gy/",
    "https://vt.tiktok.com/ZSYwJyRx6/",
    "https://vt.tiktok.com/ZSYck9hJL/",
    "https://vt.tiktok.com/ZSYck5VNy/",
    "https://vt.tiktok.com/ZS2fogfNn/",
    "https://vt.tiktok.com/ZS2oCsmDC/",
    "https://vt.tiktok.com/ZSYwJjdPx/",
    "https://vt.tiktok.com/ZSYwJd4yE/",
    "https://vt.tiktok.com/ZSYyyVDLy/",
    "https://vt.tiktok.com/ZSYwJ8hQU/",
    "https://vt.tiktok.com/ZSYckPXhv/",
    "https://vt.tiktok.com/ZS2foyKxb/",
    "https://vt.tiktok.com/ZSYckrTd5/",
    "https://vt.tiktok.com/ZS21VMtWh/",
    "https://vt.tiktok.com/ZS2foVwR1/",
    "https://vt.tiktok.com/ZSYbMTpnM/",
    "https://vt.tiktok.com/ZSYwJDNr7/",
    "https://vt.tiktok.com/ZS21VkHGV/",
    "https://vt.tiktok.com/ZS2fohKHM/",
    "https://vt.tiktok.com/ZS2foh6Qt/",
    "https://vt.tiktok.com/ZSYwJ22M6/",
    "https://vt.tiktok.com/ZSYckDkfH/",
    "https://vt.tiktok.com/ZS2fo9rQt/",
    "https://vt.tiktok.com/ZSYwJFTDU/",
    "https://vt.tiktok.com/ZSYbrC8nh/",
    "https://vt.tiktok.com/ZS2foho44/",
    "https://vt.tiktok.com/ZSYwJSjeb/",
    "https://vt.tiktok.com/ZSYwJ6v33/",
    "https://vt.tiktok.com/ZSYmyUALF/",
    "https://vt.tiktok.com/ZS2foAhjF/",
    "https://vt.tiktok.com/ZSYckNKsc/",
    "https://vt.tiktok.com/ZS2foCuuR/",
    "https://vt.tiktok.com/ZSYyyP76G/",
    "https://vt.tiktok.com/ZSYwJNcHs/",
    "https://vt.tiktok.com/ZSYck5Xx1/",
    "https://vt.tiktok.com/ZS2foB4Ja/",
    "https://vt.tiktok.com/ZSYJ8xjJ8/",
    "https://vt.tiktok.com/ZSYwJA9Cj/",
    "https://vt.tiktok.com/ZSYwJ8pqg/",
    "https://vt.tiktok.com/ZSYck66Tu/",
    "https://vt.tiktok.com/ZS21VLd9B/",
    "https://vt.tiktok.com/ZS2foDBht/",
    "https://vt.tiktok.com/ZS2foyvdM/",
    "https://vt.tiktok.com/ZSYck98TH/",
    "https://vt.tiktok.com/ZSFo4K6po/",
    "https://www.tiktok.com/@a_ki.03/video/7359940125935078674?_t=8m4JfhjupO8&amp;_r=1",
    "https://vt.tiktok.com/ZSY9eKkYG/",
    "https://vt.tiktok.com/ZS2o4xUWQ/",
    "https://vt.tiktok.com/ZS2foSu3u/",
    "https://vt.tiktok.com/ZS2foScoq/",
    "https://www.tiktok.com/@leleyspam/video/7379173272069393665?_r=1&amp;u_code=e275f59dg9eiib&amp;region=PH&amp;mid=7196818686223715078&amp;preview_pb=0&amp;sharer_language=en&amp;_d=dl4ad62m31bah3&amp;share_item_id=7379173272069393665&amp;source=h5_t&amp;timestamp=1722981326&amp;user_id=7107242558354474010&amp;sec_user_id=MS4wLjABAAAA-cPSGip-M0kC_JB4WQt8XGxH4I0mgTbqqDO4ANoTrWwdgHh9GDU7PzvKZgYgfQq1&amp;social_share_type=0&amp;utm_source=copy&amp;utm_campaign=client_share&amp;utm_medium=android&amp;share_iid=7355345020910634758&amp;share_link_id=6664c40a-1928-4ef2-80ae-c22adba6a7f6&amp;share_app_id=1180&amp;ugbiz_name=MAIN&amp;ug_btm=b8727%2Cb2878&amp;enable_checksum=1",
    "https://vt.tiktok.com/ZS2fo44j6/",
    "https://vt.tiktok.com/ZSYwJNgkM/",
    "https://vt.tiktok.com/ZS2foPpoq/",
    "https://vt.tiktok.com/ZSYwJr5tm/",
    "https://vt.tiktok.com/ZSYckLvso/",
    "https://vt.tiktok.com/ZS214oG1V/",
    "https://vt.tiktok.com/ZSYwJe3nk/",
    "https://vt.tiktok.com/ZSYchvrXV/",
    "https://vt.tiktok.com/ZSYwJk6aA/",
    "https://vt.tiktok.com/ZS21V1G6E/",
    "https://vt.tiktok.com/ZSYckNxx8/",
    "https://vt.tiktok.com/ZS2oQwfbb/",
    "https://vt.tiktok.com/ZSYcka5so/",
    "https://vt.tiktok.com/ZS2oXrvj3/",
    "https://vt.tiktok.com/ZS2fousGK/",
    "https://vt.tiktok.com/ZS2foBxRE/",
    "https://vt.tiktok.com/ZS214TqtJ/",
    "https://vt.tiktok.com/ZS2foBNYP/",
    "https://vt.tiktok.com/ZS21V8CA7/",
    "https://vt.tiktok.com/ZS21Vkxse/",
    "https://vt.tiktok.com/ZSYckMTW2/",
    "https://vt.tiktok.com/ZSY9d16oQ/",
    "https://vt.tiktok.com/ZS2foBL6a/",
    "https://vt.tiktok.com/ZS2o75gXC/",
    "https://vt.tiktok.com/ZS2H413aA/",
    "https://vt.tiktok.com/ZS2foBjSN/",
    "https://vt.tiktok.com/ZS21VhKwB/",
    "https://vt.tiktok.com/ZSY9d1Xor/",
    "https://vt.tiktok.com/ZS214TFw5/",
    "https://vt.tiktok.com/ZSYwJAX3H/",
    "https://vt.tiktok.com/ZSYckBJhd/",
    "https://www.tiktok.com/@leiangeleecruz613/video/7393996938212805906?_r=1&amp;u_code=e275f59dg9eiib&amp;region=PH&amp;mid=7370521417198488325&amp;preview_pb=0&amp;sharer_language=en&amp;_d=dl4ad62m31bah3&amp;share_item_id=7393996938212805906&amp;source=h5_t&amp;timestamp=1722981310&amp;user_id=7107242558354474010&amp;sec_user_id=MS4wLjABAAAA-cPSGip-M0kC_JB4WQt8XGxH4I0mgTbqqDO4ANoTrWwdgHh9GDU7PzvKZgYgfQq1&amp;social_share_type=0&amp;utm_source=copy&amp;utm_campaign=client_share&amp;utm_medium=android&amp;share_iid=7355345020910634758&amp;share_link_id=ff9b67d6-15ad-41b6-a9d7-a50931f42034&amp;share_app_id=1180&amp;ugbiz_name=MAIN&amp;ug_btm=b8727%2Cb2878&amp;enable_checksum=1",
    "https://vt.tiktok.com/ZSYckBfWC/",
    "https://vt.tiktok.com/ZSYPsuavp/",
    "https://www.tiktok.com/@akiyaaah/video/7344749544594312453?_t=8m4JolsnJ3N&amp;_r=1",
    "https://vt.tiktok.com/ZSFoGrmFu/",
    "https://vt.tiktok.com/ZS2fokMFt/",
    "https://vt.tiktok.com/ZS2fokvME/",
    "https://vt.tiktok.com/ZS21VRyBf/",
    "https://vt.tiktok.com/ZS2foCBev/",
    "https://vt.tiktok.com/ZS2fouWwG/",
    "https://vt.tiktok.com/ZS21VNk2k/",
    "https://vt.tiktok.com/ZS2foD1DA/",
    "https://vt.tiktok.com/ZSYbr21cQ/",
    "https://vt.tiktok.com/ZS2foaLFA/",
    "https://vt.tiktok.com/ZS2foHyen/",
    "https://vt.tiktok.com/ZS2foQGv2/",
    "https://vt.tiktok.com/ZS2fohmT9/",
    "https://vt.tiktok.com/ZSYckruUY/",
    "https://vt.tiktok.com/ZS2foBDj4/",
    "https://www.tiktok.com/@alexisxz8/video/7360968137463958789?_t=8m90uBxWpOb&amp;_r=1",
    "https://www.tiktok.com/@uluvsdrake/video/7364810622481026309?_t=8m90wxBNw0I&amp;_r=1",
    "https://vt.tiktok.com/ZSYyyHeMV/",
    "https://vt.tiktok.com/ZS2oHnf5T/",
    "https://vt.tiktok.com/ZS2foyS27/",
    "https://vt.tiktok.com/ZSYV22YTF/",
    "https://vt.tiktok.com/ZSYwJ28Db/",
    "https://vt.tiktok.com/ZSYwJe7Ye/",
    "https://vt.tiktok.com/ZS21V2W2y/",
    "https://vt.tiktok.com/ZS2oQEknj/",
    "https://vt.tiktok.com/ZS2oQdmAN/",
    "https://vt.tiktok.com/ZSYw1oKPo/",
    "https://vt.tiktok.com/ZSYwJ16at/",
    "https://vt.tiktok.com/ZSYbrjvyV/",
    "https://vt.tiktok.com/ZSYJRYC5j/",
    "https://vt.tiktok.com/ZS2oXDf4y/",
    "https://vt.tiktok.com/ZS214oxY5/",
    "https://vt.tiktok.com/ZSYV2MFt3/",
    "https://vt.tiktok.com/ZSYckmDd6/",
    "https://vt.tiktok.com/ZS2foXYTX/",
    "https://vt.tiktok.com/ZSYwJFXXt/",
    "https://vt.tiktok.com/ZS2oQpr3x/"
]

url = "https://api.joshweb.click/tiktokdl?url="
def shoti(bot, data):
  if data.args:
    return bot.sendMessage("⚠️ This command dont need an argument.")
  loading = bot.sendMessage("⏳ Generating a random shoti video...")
  try:
    res = get(url + choice(LISTAHAN)).json()
    if "error" in res:
      bot.unsendMessage(loading['id'])
      return bot.sendMessage("⚠️ An error accured while fetching the data, please try again.")
    message = {
      "body": f"━━━━━━━━━━━━━━━\n{res['description']}\n━━━━━━━━━━━━━━━" if res['description'] != 'No Description' else None,
      "attachment": {
        "src": res['url'],
        "type": 'video'
      }
    }
    bot.unsendMessage(loading['id'])
    return bot.sendMessage(message)
  except Exception as e:
    print("ERROR: ", e)
    bot.unsendMessage(loading['id'])
    return bot.sendMessage("⚠️ An error accured while fetching the data, please try again.")

config = {
  "name": 'shoti',
  "def": shoti,
  "description": 'Generate a random sexy girl videos',
  "credits": 'Greegmon'
}