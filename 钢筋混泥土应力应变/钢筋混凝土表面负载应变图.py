import pandas as pd
import numpy as np
from pyecharts.charts import Line
from pyecharts import options as opts
import warnings

xlsx_path = "datasets.xlsx"
df = pd.read_excel(xlsx_path, sheetname=4)

data = [[0 for i in range(5)] for i in range(2)]
k = 0
for i in range(2):
    for j in range(5):
        #print(i,j)
        data[i][j] = df.ix[1:50, 0+k*4:3+k*4]
        k = k + 1
# 构建二维数组导入数据
warnings.filterwarnings("ignore")
# 忽略ix方法的warning

data_listx = [[0 for i in range(5)] for i in range(2)]
data_listy = [[0 for i in range(5)] for i in range(2)]

n = 0
m = 0
data_index = ['1-1-C15', '1-2-C15', '1-3-C15', '1-4-C40', '1-5-C40', '2-1-C30', '2-2-C30', '2-3-C50', '2-4-C50', '2-5-C50']

try:
    for i in range(2):
        for j in range(5):
            data_listx[i][j] = data[i][j]['Unnamed: {}'.format(2+n)].astype(float).round(6).tolist()
            n = n + 4
except KeyError:
    pass

try:
    for i in range(2):
        for j in range(5):
            data_listy[i][j] = data[i][j][data_index[m]].astype(float).round(2).tolist()
            n = n + 4
            m = m + 1
except KeyError:
    pass
# 将数据转换为pyecharts支持的数据类型

line = (
        Line()
        .add_xaxis(data_listx[0][0])                            # 设置x轴数据
        .add_yaxis('1-1-C15', data_listy[0][0],                 # 设置y轴数据并调整样式
            label_opts=opts.LabelOpts(is_show=False),           # 不显示标签数据
            linestyle_opts=opts.LineStyleOpts(),                # 设置线的样式，暂不设置
            itemstyle_opts=opts.ItemStyleOpts(opacity=0),       # 将标签点的透明度设置为100%
            color='#000000',  # 1-1-C15为纯黑                   # 设置线条颜色
            #is_smooth=True
        )
        .add_xaxis(data_listx[0][1])
        .add_yaxis('1-2-C15', data_listy[0][1],
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(),
            itemstyle_opts=opts.ItemStyleOpts(opacity=0),
            color='	#808080',  # 1-2-C15为灰色
            #is_smooth=True
        )
        .add_xaxis(data_listx[0][2])
        .add_yaxis('1-3-C15', data_listy[0][2],
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(),
            itemstyle_opts=opts.ItemStyleOpts(opacity=0),
            color='#8B0000',  # 1-3-C15为深红色
            #is_smooth=True
        )
        .add_xaxis(data_listx[0][3])
        .add_yaxis('1-4-C40', data_listy[0][3],
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(),
            itemstyle_opts=opts.ItemStyleOpts(opacity=0),
            color='#FFA500',  # 1-4-C40为橙色
            #is_smooth=True
        )
        .add_xaxis(data_listx[0][4])
        .add_yaxis('1-5-C40', data_listy[0][4],
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(),
            itemstyle_opts=opts.ItemStyleOpts(opacity=0),
            color='#808000',  # 1-5-C40为橄榄
            #is_smooth=True
        )
        .add_xaxis(data_listx[1][0])
        .add_yaxis('2-1-C30', data_listy[1][0],
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(),
            itemstyle_opts=opts.ItemStyleOpts(opacity=0),
            color='#008000',  # 2-1-C30为纯绿
            #is_smooth=True
        )
        .add_xaxis(data_listx[1][1])
        .add_yaxis('2-2-C30', data_listy[1][1],
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(),
            itemstyle_opts=opts.ItemStyleOpts(opacity=0),
            color='#48D1CC',  # 2-2-C30为中绿宝石
            #is_smooth=True
        )
        .add_xaxis(data_listx[1][2])
        .add_yaxis('2-3-C50', data_listy[1][2],
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(),
            itemstyle_opts=opts.ItemStyleOpts(opacity=0),
            color='#1E90FF',  # 2-3-C50为闪兰色
            #is_smooth=True
        )
        .add_xaxis(data_listx[1][3])
        .add_yaxis('2-4-C50', data_listy[1][3],
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(),
            itemstyle_opts=opts.ItemStyleOpts(opacity=0),
            color='#8B008B',  # 2-4-C50为深洋红
            #is_smooth=True
        )
        .add_xaxis(data_listx[1][4])
        .add_yaxis('2-5-C50', data_listy[1][4],
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(),
            itemstyle_opts=opts.ItemStyleOpts(opacity=0),
            color='#FF1493',  # 2-5-C50为深粉红
            #is_smooth=True
        )

        .set_global_opts(                                        # 设置全局样式
            title_opts=opts.TitleOpts(
                title='钢筋混凝土表面负载应变图',
                pos_bottom='0',
                pos_right='30%'
            ),
            xaxis_opts=opts.AxisOpts(
                type_='value',
                boundary_gap=False,
                name="平均应变"
            ),                                                    # 设置x轴类型属性为value数值类型
            yaxis_opts=opts.AxisOpts(                             # 单轴配置项
                name="负载 P,kN",
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),    # 显示坐标轴刻度
                splitline_opts=opts.SplitLineOpts(is_show=True)   # 显示分割线
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                trigger="axis",
                trigger_on="mousemove|click",
                axis_pointer_type="cross"                          # 启用十字准星指示器
            ),
            toolbox_opts=opts.ToolboxOpts(                         # 工具箱，支持区域缩放和图片下载
                is_show=True,
                pos_bottom = '90%',
                feature={
                        "dataZoom": {"yAxisIndex": "none"},
                        "restore": {},
                        "saveAsImage": {}
                        }
            )
        )
    )

# jupyter在线生成图像
#line.render_notebook()
# 本地生成html文件
line.render('钢筋混凝土表面负载应变图.html')
