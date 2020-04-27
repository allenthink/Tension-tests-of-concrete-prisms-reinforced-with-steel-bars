import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts
import warnings

xlsx_path = "datasets.xlsx"
df = pd.read_excel(xlsx_path, sheetname=3)
data1 = df.ix[3:52, (0,5)]
data2 = df.ix[3:52, (0,10)]
# 从excel中采集数据
warnings.filterwarnings("ignore")
# 忽略ix方法的warning

data_listy1 = data1['Prism 1-1-C15'].astype(float).round(2).tolist()
data_listx1 = data1['Unnamed: 5'].astype(float).round(4).tolist()
data_listy2 = data2['Prism 1-1-C15'].astype(float).round(2).tolist()
data_listx2 = data2['Unnamed: 10'].astype(float).round(4).tolist()
# 将数据转换为pyecharts支持的数据类型
#print(data_listx1)
#print(data_listx2)

line = (
        Line()
        .add_xaxis(data_listx1)                                 # 设置x轴数据
        .add_yaxis('混凝土表面平均形变', data_listy1,                        # 设置y轴数据并调整样式
            label_opts=opts.LabelOpts(is_show=False),           # 不显示标签数据
            linestyle_opts=opts.LineStyleOpts(),                # 设置线的样式，暂不设置
            itemstyle_opts=opts.ItemStyleOpts(opacity=0),       # 将标签点的透明度设置为100%
            color='#0000FF'  # Ø10-3为蓝色                      # 设置线条颜色
        )
        .add_xaxis(data_listx2)  # 设置x轴数据
        .add_yaxis('钢筋混凝土表面平均形变', data_listy2,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(),
            itemstyle_opts=opts.ItemStyleOpts(opacity=0),
            color='#00FF00'  # Ø10-1为绿色
        )

        .set_global_opts(                                        # 设置全局样式
            title_opts=opts.TitleOpts(
                title='受压形变量',
                pos_bottom='0',
                pos_right='35%'
            ),
            xaxis_opts=opts.AxisOpts(
                type_='value',
                boundary_gap=False,
                name="平均形变量 Δ,mm"
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
line.render('受压形变量.html')
