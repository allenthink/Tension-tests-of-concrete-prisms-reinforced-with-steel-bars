import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts
import warnings

xlsx_path = "datasets.xlsx"
df = pd.read_excel(xlsx_path, sheetname=2)
data1 = df.ix[2:331,  :2]
data2 = df.ix[2:349, 2:4]
data3 = df.ix[2:332, 4:6]
# 从excel中采集三组数据
warnings.filterwarnings("ignore")
# 忽略ix方法的warning

data_listx1 = data1['Strain'].astype(float).round(4).tolist()
data_listx2 = data2['Strain.1'].astype(float).round(4).tolist()
data_listx3 = data3['Strain.2'].astype(float).round(4).tolist()
data_listy1 = data1['Stress'].astype(float).round(2).tolist()
data_listy2 = data2['Stress.1'].astype(float).round(2).tolist()
data_listy3 = data3['Stress.2'].astype(float).round(2).tolist()
# 将数据转换为pyecharts支持的数据类型

line = (
        Line()
        .add_xaxis(data_listx1)                                 # 设置x轴数据
        .add_yaxis('Ø10-1', data_listy1,                        # 设置y轴数据并调整样式
            label_opts=opts.LabelOpts(is_show=False),           # 不显示标签数据
            linestyle_opts=opts.LineStyleOpts(),                # 设置线的样式，暂不设置
            itemstyle_opts=opts.ItemStyleOpts(opacity=0),       # 将标签点的透明度设置为100%
            color='#FF0000'  # Ø10-1为蓝色                      # 设置线条颜色
        )
        .add_xaxis(data_listx2)
        .add_yaxis('Ø10-2', data_listy2,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(),
            itemstyle_opts=opts.ItemStyleOpts(opacity=0),
            color='#00FF00'  # Ø10-2为绿色
        )
        .add_xaxis(data_listx3)
        .add_yaxis('Ø10-3', data_listy3,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(),
            itemstyle_opts=opts.ItemStyleOpts(opacity=0),
            color='#0000FF'  # Ø10-3为红色
        )

        .set_global_opts(                                        # 设置全局样式
            title_opts=opts.TitleOpts(
                title='钢筋的应力应变图',
                pos_bottom='0',
                pos_right='35%'
            ),
            xaxis_opts=opts.AxisOpts(
                type_='value',
                boundary_gap=False,
                name="拉伸应变ε,mm"
            ),                                                    # 设置x轴类型属性为value数值类型
            yaxis_opts=opts.AxisOpts(                             # 单轴配置项
                name="应力σ,MPa",
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
line.render('钢筋的应力应变图.html')
