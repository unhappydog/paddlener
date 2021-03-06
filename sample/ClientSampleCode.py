import sys
sys.path.append("..")
from core.consulclient import Client


if __name__ == '__main__':
    client = Client("paddleserver")
    datas = """2019年8月29日，备受业界关注的“2019世界人工智能大会”在上海拉开帷幕。比尔·盖茨曾说“语言理解是人工智能皇冠上的明珠
。自然语言处理的进步将会推动人工智能整体进展。”8月30日，由达观数据和乐言科技联合主办的《理解语言，拥抱智能》主题论坛在上海世博中心重磅开启。
　　长宁区委常委、副区长、区政府党组副书记钟晓敏，浦东新区副区长管小军，国际计算语言学(ACL)终身成就奖得主、中国中文信息学会名誉理事长李生
教授出席本次活动，论坛同时还邀请到伊利诺伊大学香槟分校教授Heng Ji，苏州大学特聘教授、国家杰出青年科学基金获得者张民，复旦大学教授、中国中文信息学会常务理事黄萱菁，中国人工智能学会常务理事、北京邮电大学教授王小捷、达观数据CEO陈运文和乐言科技CEO沈李斌多位世界级AI领袖，与现场来宾分享人工智能发展的独到深刻观点。本次论坛从自然语言处理出发，围绕语言智能的学术与应用展开了最前沿和务实的讨论。
　　达观数据创始人陈运文博士以《具备语义智能理解的RPA流程机器人》为题，分享了自然语言处理技术目前在工业界的应用，他谈到“文字的自动化处理面临一个非常好的机遇。深度神经网络的技术从2006年由Hinton教授提出来以后，经过十多年的发展越来越来成熟，尤其是用在文本智能处理领域。他介绍通过将NLP技术与机器人流程自动化(RPA)结合，可以赋予机器人阅读思考的能力，在现有各类工作系统中协助完成阅读撰写等流程性的重复工作。目前达观数据在商业案例报告生成、智慧政务行政审批、金融文档验查和填写等场景中，推出的机器人员工已逐步开展各项工作。”
　　乐言科技创始人沈李斌博士以《认知智能赋能企业计算》为题，分享了以自然语言处理、知识图谱、机器学习为核心的认知智能技术在企业计算中的广泛应用。
　　在大会期间，世界人工智能大会WAIC联合达观数据联合推出了AI新闻助手，该助手集成自然语言处理(NLP)与光学字符识别(OCR)技术，让文字工作者们在文章素材采集转写、自动摘要撰写、内容分类等方面体验人工智能的便捷。
　　该助手还可快速做出符合规范的五言、七言绝句，绝句灵活轻便，声调平仄相对。据达观数据创始人陈运文介绍，新闻助手对五万余首全唐诗进行了“语料”学习，通过生成语义分析模型，并经过不断训练后，最终具备“出口成章”的能力。
　前不久，达观数据发布了国内首款自主研发集 NLP(自然语言处理)与OCR(光学字符识别)于一体的达观智能RPA。通过让让计算机学习和模仿人类处理任务的步骤，协助完成重复性的文书操作工作，为企业打造智能数字化员工。
　　语言作为人类交流的重要方式，人工智能将如何破译人类语言的密码?在智能化技术的发展过程中，自然语言处理技术助推各行业催生的新产品为生产力带来了质的飞跃。
　　语言智能作为人工智能发展中的核心 ，将改变我们在工作中对文档内容的阅读、审阅和生产方式。随着自然语言处理技术的发展和应用，人机协作的未来有很大想象空间。"""
    datas = datas.replace('\n','').replace('\u3000', '').replace('\n', '')
    a = client("ner", datas)
    print(a)
