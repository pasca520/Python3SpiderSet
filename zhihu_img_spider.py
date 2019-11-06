# -*- coding: utf-8 -*-
import requests
import re
import math
import os
import random
import string
import time
from qiniu import Auth
from qiniu import BucketManager


# 爬虫主体
def get_page(url, limit, offset):
    headers = {
        'authority': 'www.zhihu.com',
        'x-ab-param': 'li_pay_banner_type=0;se_new_topic=0;ug_goodcomment_0=1;zw_sameq_sorce=999;zr_paid_answer_mix=mixed_20;se_backsearch=0;tp_qa_metacard=1;ug_follow_answerer=0;li_video_section=1;qap_ques_invite=0;se_webtimebox=1;se_amovietab=1;se_featured=1;soc_zcfw_shipinshiti=0;se_dnn_mt=0;se_entity_model=0;se_search_feed=N;se_ctr_pyc=0;se_billboardsearch=0;se_college_cm=1;tsp_hotlist_ui=3;ug_newtag=1;zr_km_special=close;zr_rec_answer_cp=close;zr_km_category=close;tp_header_style=1;tsp_vote=2;soc_zcfw_broadcast=0;ug_follow_answerer_0=0;ls_new_upload=1;ls_videoad=2;zr_cold_start=4;se_movietab=1;tp_sft=a;tsp_hotctr=1;tsp_billboardsheep2=2;top_test_4_liguangyi=1;tp_topic_head=0;zw_payc_qaedit=0;zr_km_recall=default;zr_infinity_member=close;se_webmajorob=0;se_sug=1;se_ltr_user=0;se_payconsult=5;li_qa_new_cover=1;se_mclick1=2;tp_sft_v2=d;top_v_album=1;tsp_newchild=4;pf_fuceng=1;se_cardrank_3=0;li_qa_cover=old;li_se_media_icon=1;zr_answer_rec_cp=open;zr_slot_cold_start=aver;se_cardrank_2=1;se_p_slideshow=0;soc_stickypush=0;pf_noti_entry_num=0;se_perf=0;tp_qa_toast=1;soc_bignew=1;soc_zcfw_badcase=0;tp_qa_metacard_top=top;li_album_liutongab=0;li_se_kv=0;li_se_xgb=0;zr_km_style=base;se_preset_tech=0;se_wannasearch=a;top_native_answer=6;ug_zero_follow=0;se_ltr_dnn_cp=0;li_purchase_test=0;zr_ans_rec=gbrank;zr_km_slot_style=event_card;zr_search_xgb=1;zr_km_recall_num=close;zr_filter=ignore_topics;se_expired_ob=0;zr_intervene=1;zr_test_aa1=0;se_zu_onebox=0;se_ctr_user=0;se_site_onebox=0;se_ltr_cp_new=1;li_se_paid_answer=0;zr_art_rec=base;se_club_post=5;se_adxtest=1;se_use_zitem=0;li_salt_hot=0;li_search_answer=3;li_se_vertical=1;zr_km_item_prerank=old;zr_km_prerank=new;zr_slotpaidexp=1;se_lottery=0;ug_fw_answ_aut_1=0;ls_zvideo_like=0;zr_rel_search=base;zr_new_commodity=0;se_spb309=0;se_waterfall=0;tp_sticky_android=2;pf_foltopic_usernum=50;se_ios_spb309=1;se_likebutton=0;se_colorfultab=1;se_cardrank_4=1;se_agency= 0;soc_special=0;soc_bigone=1;ug_follow_topic_1=2;qap_payc_invite=0;se_mobileweb=1;se_time_threshold=0;top_universalebook=1;soc_zuichangfangwen=6;ls_zvideo_license=0;se_sepciality=0;tsp_billboardhead=2;li_se_album_card=0;se_websearch=3;tsp_childbillboard=2;sem_up_growth=in_app;zr_video_rank=new_rank;zr_man_intervene=0;zr_prerank_heatscore=false;se_whitelist=1;tp_club_qa=1;ls_zvideo_trans=0;zr_km_item_cf=open;se_go_ztext=0;se_ctx=0;se_pro=0;pf_newguide_vertical=0;ug_zero_follow_0=0;se_auto_syn=0;top_new_feed=5;pf_creator_card=1;li_android_vip=0;zr_recall_heatscore=false;se_dnn_unbias=1;se_subtext=1;tp_club_qa_pic=1;li_hot_score_ab=0;li_vip_no_ad_mon=0;zr_article_new=close;se_hotsearch=1;top_ebook=0;se_cardrank_1=0;se_ad_index=10;tp_meta_card=0;soc_update=1;tp_m_intro_re_topic=1;li_se_heat=1;li_book_button=0;zr_video_rank_nn=new_rank;se_mclick=0;se_time=0.5;se_ab=0;se_zu_recommend=0;top_vipconsume=1;soc_notification=1;ls_fmp4=0;top_hotcommerce=1;top_ydyq=X;zr_km_answer=open_cvr;zr_video_recall=current_recall;zr_km_feed_prerank=new;se_hotmore=0;se_aa_base=1;se_college=default;li_se_section=0;zr_item_nn_recall=close;zr_km_topic_zann=new;se_webrs=1;se_topicfeed=0;se_bst=0;li_qa_btn_text=0;zr_km_feed_nlp=old;se_col_boost=0;soc_yxzl_zcfw=0;li_tjys_ec_ab=0;se_topiclabel=1;se_ctr_topic=0;se_hot_timebox=1;se_famous=1;top_quality=0;top_root=0',
        'x-requested-with': 'fetch',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        'cookie': '_zap=1e68d90d-24bc-466c-abaa-95b3742f7c5d; _xsrf=E53NvZThal0kfH2AIUDeqncRPeqoN6Wn; d_c0="AKCoTa74bw-PTntcCBsmKGuUufXYZkQblEE=|1557992311"; UM_distinctid=16ba3957d4448f-0ffe346615062f-37627e03-13c680-16ba3957d456ba; __utma=51854390.1918436468.1563268856.1563268856.1563268856.1; __utmz=51854390.1563268856.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/hot; __utmv=51854390.100-1|2=registration_date=20150917=1^3=entry_date=20150917=1; tst=r; q_c1=9a76ab9b024b4aca95937abb63762fdf|1570515114000|1558948626000; capsion_ticket="2|1:0|10:1572334589|14:capsion_ticket|44:MmFkOGVhN2I3N2RmNDU5ZWFjNTdhODBhNGNjNjhjZTM=|0ffb0e69befc1d3e70223353f74ca767fc9bbee629e0b923e8c16e36993dd60f"; z_c0="2|1:0|10:1572334607|4:z_c0|92:Mi4xVTZZWkFnQUFBQUFBb0toTnJ2aHZEeVlBQUFCZ0FsVk5EenFsWGdBbFJOZXpnRlhSYVNQU0JsSlg2Tng1V2hLV0RR|81669400aa05bf5ea49358713ca696c3c9dc625e991730ac04ba8531d0dcc983"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1572838565,1572848709,1572864099,1572865376; CNZZDATA1272960301=797563411-1561816893-https%253A%252F%252Fwww.google.com.hk%252F%7C1572924243; tgw_l7_route=fd63c3ae6724333eae94c71ab6d69628; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1572926421',
    }

    params = (
        ('include',
         'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info,paid_info_content;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics'),
        ('limit', limit),
        ('offset', offset),
        ('platform', 'desktop'),
        ('sort_by', 'default'),
    )
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if not data['data']:
            print('没有数据！(%s)' % url)
        else:
            return data, data["paging"]["totals"]
    else:
        print('返回值: %s, url: %s' % (response.status_code, url))


# 解析网页模块
def parse_json(data):
    # urls_one_set = []
    for info in data["data"]:
        # name = info["author"]["name"]
        pattern = re.compile(r'img src=\"(https://.*?)\"', re.S)
        urls = re.findall(pattern, info['content'])
        # urls_one_set.extend(urls)  # 在列表末尾一次性追加另一个序列中的多个值，即将每页的链接放入一个列表返回
        yield from urls


# 下载图片，保存到本地
def download_img(urls_one_set, title, num):
    file_path = './img'
    # local_time = time.strftime('%Y_%m_%d_%H:%M:%S', time.localtime(time.time()))
    try:
        os.makedirs(file_path, exist_ok=True)
        for img_url in urls_one_set:
            num += 1
            random_string = ''.join(
                random.choices(
                    string.ascii_letters +
                    string.digits,
                    k=15))
            with open('./img/{}|{}|{}.jpg'.format(num, title, random_string), 'wb') as f:
                res = requests.get(img_url)
                f.write(res.content)
            print("正在保存第%s张图片" % num)
        time.sleep(5)  # 休息下，毕竟学习，对让人家服务器xxx了
        return num  # 必须返回 num，否则局部变量 num 自增的值不生效
    except IOError as e:
        print("写入失败", e)
    except Exception as e:
        print("发生错误", e)


# 保存到七牛云存储, 官网文档查看 fetch 接口：https://developer.qiniu.com/kodo/sdk/1242/python
def save_qiniu(urls_one_set, title, num):
    access_key = 'xxxxx'  # 七牛的 ak，打开https://portal.qiniu.com/user/key获得
    secret_key = 'xxxxx'  # 七牛的 sk, 打开https://portal.qiniu.com/user/key获得
    bucket_name = 'app-download'
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)
    for img_url in urls_one_set:
        num += 1
        local_time = time.strftime('%Y_%m_%d', time.localtime(time.time()))
        random_string = ''.join(
            random.choices(
                string.ascii_letters +
                string.digits,
                k=15))
        key = '{}/{}|{}|{}.jpg'.format(local_time, num, title, random_string)
        ret, info = bucket.fetch(img_url, bucket_name, key)
        print("正在保存第%s张图片" % num)
    assert ret['key'] == key
    return num


if __name__ == '__main__':
    offset = 5  # 页数，0代表第一页
    limit = 5  # 一页几个回答
    num = 0  # 初始下载数

    # 知乎文章回答数平均3k以上
    ZhiHuArticle = {
        '305888519': '女生素颜能漂亮到什么程度？',
        '50426133': '平常人可以漂亮到什么程度？',
        '34243513': '你见过最漂亮的女生长什么样？',
        '285321190': '拥有一双大长腿是怎样的体验？',
        '26037846': '身材好是一种怎样的体验？',
        '333026642': '女生什么样的身材算是好身材？'
    }
    for key in ZhiHuArticle.keys():
        url = 'https://www.zhihu.com/api/v4/questions/{}/answers'.format(key)
        title = ZhiHuArticle[key]
        json_data, answer_totals = get_page(url, limit, offset)
        all_pages = math.ceil(answer_totals / offset)  # 先精确除，然后值向上取整
        for next_page in range(0, all_pages * 5, 5):
            json_data, answer_totals = get_page(url, limit, next_page)
            urls_one_set = parse_json(json_data)
            # num = download_img(urls_one_set, title, num)
            num = save_qiniu(urls_one_set, title, num)
    print('待爬问题页爬取结束，欢迎下次再来！')
