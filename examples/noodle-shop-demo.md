# 示例：30秒虚构面馆宣传片

这是为了说明交付格式而编写的演示，不是已运行完整Agent流程的测试报告，也没有生成或验证图片、声音和视频。店名、卖点与对话均为虚构，与任何真实门店无关。

## 输入与需求沟通示例

用户：“我想给一家面馆做30秒AI宣传片，发竖屏平台。”

策划首轮：“主要给谁看？你希望他们最记住什么？”

演示回答：“附近上班族，记住现煮热面适合午餐。”

接下来分轮确认菜品、门店气质、画幅、素材、边界；不一次替用户决定全部需求。

## 1. 创作需求卡（演示假设）

- 虚构店名：一碗热面。
- 观众：附近上班族；目的：形成午餐选择记忆。
- 核心表达：午间稍作停顿，一碗现煮热面。
- 形式：30秒商业美食片，9:16，自然写实，温暖明亮。
- 声音：环境声与音乐，不含对白或旁白；不需要人物试音资产。
- 菜品：清汤葱花面。无价格、出餐时效、销量及认证承诺。
- 条件：无现成图片；本示例先出标明缺图的文字草案。

## 2. 剧本文件选择与大纲

建议只写一份详细大纲：故事不依赖人物背景，无需人物小传；三个内容段已能表达结构。真实使用时先获得用户确认，再编写。

|成片时间|内容与动作|表达|
|---|---|---|
|0—10秒|午间门外光影→厨房提起面条→热面落入碗中|从忙碌进入现煮过程|
|10—20秒|舀汤→葱花落下→将碗放到传菜台|让食物成为视觉中心|
|20—30秒|完整成菜→自然轻推→片尾品牌版式|记住一碗面与店名|

文字层由后期叠加，不让视频模型生成店名。

## 3. 资产清单与英文提示词

|编号|内容|版本/状态|
|---|---|---|
|C01|不发声的厨师，仅手部出镜|设定v1；图片未生成|
|E01|厨房：左后灶台、中央传菜台、右侧出口|布局v1；俯视图未生成|
|P01|哑光白色陶瓷面碗|设定v1；图片未生成|
|F01|白碗清汤面、少量葱花，无其他配菜|外观v1；图片未生成|

### C01 人物参考板

```text
Create a cinematic photorealistic character reference sheet, 9:16 portrait canvas, 2x2 panels with a shorter upper row and taller lower row. The same fictional East Asian adult chef in all views, short black hair, ivory shirt, charcoal apron, natural skin texture. Upper left: frontal face close-up. Upper right: side-profile face close-up. Lower left: body below the head, front view, including footwear. Lower right: body below the head, rear view, including footwear. Clean solid studio background, soft rim lighting. No props, no text. Keep identity, clothing and body proportions consistent.
```

### E01 总环境俯视图

```text
Create a photorealistic overhead spatial reference of one compact contemporary noodle-shop kitchen, 9:16 canvas. Fix north at the top: stainless steel cooking station along the northwest wall, central wooden serving counter, unobstructed aisle to an exit on the east wall. Soft daylight from the south window, neutral materials and realistic proportions. Show the complete layout clearly, no people, no text or arrows. This image establishes the spatial reference for later views.
```

### E01 场景四宫格草案

俯视图确认前，本提示词仅为布局假设；生成时提供确认的俯视图作为参考。

```text
Create a cinematic photorealistic environment reference sheet on a 9:16 canvas with four equal 2x2 panels. Use the supplied confirmed overhead layout of the SAME noodle-shop kitchen. Upper left: wide view from the southeast corner toward the northwest stove and central counter. Upper right: reverse view from the northwest toward the south window. Lower left: view from the west side of the central counter toward the east exit. Lower right: view from the east exit toward the central counter. Preserve every fixed wall, opening and furniture position. Bright natural daylight, consistent neutral materials, no people, no text.
```

### P01 道具参考板

```text
Create a cinematic photorealistic prop reference sheet, 9:16 portrait canvas, 2x2 panels with a shorter upper row and taller lower row. Show the SAME plain matte-white ceramic noodle bowl with a rounded lip, gently tapered body and a small circular foot. Upper left: close-up of the rim. Upper right: close-up of the ceramic surface and base detail. Lower left: entire bowl, front view. Lower right: entire bowl, rear view. Clean solid studio background, soft rim lighting, no people, no unrelated objects, no food, no text. Keep dimensions, material and shape consistent.
```

### F01 成菜镜头参考

```text
A single cinematic photorealistic close-up, 9:16 portrait. The confirmed matte-white bowl contains thin wheat noodles in clear broth with a small amount of finely chopped scallion, no meat or extra toppings. On the central serving counter of the confirmed kitchen, soft daylight from the south window, natural restrained steam. Keep the bowl and kitchen consistent with the supplied references. No people, no text. This is a shot reference, not a multi-panel sheet.
```

## 4. Seedance 中文时间轴草案

所有图片尚未生成。以下用固定编号表达设计依赖，实际上传位置待用户提供，不是已完成绑定的生产提示词。C01使用局部手部参考，E01/P01使用相关单格或单张图，不直接将整张展示板当成一个镜头。

### S01：0—10秒

画幅9:16，自然写实。参考：E01厨房、C01手部、P01碗；上传映射待填。仅环境声，不说话。

- 00:00—00:03：全景，门外平视固定镜位，午间光影落在入口，厨房声提前进入；硬切。
- 00:03—00:06：近景，西北灶台侧面，C01双手将已煮好的面条轻提离水，固定机位，水滴自然落下；沸水声；硬切。
- 00:06—00:10：特写，从中央传菜台西侧略俯拍，面条落入P01碗，手部动作克制，碗保持稳定；轻微器皿声。结束：面已入碗、尚未加汤。

### S02：10—20秒

参考：E01中央传菜台、C01手部、P01及F01外观；上传映射待填。延续上一段面条形态和碗的位置。

- 00:00—00:04：特写，保持前段机位方向，C01向P01舀入清汤，一次自然倒入，轻微水声；硬切。
- 00:04—00:07：微距，焦点在汤面，少量葱花落下，不新增肉或其他配料；自然轻响；硬切。
- 00:07—00:10：中近景，中央传菜台平视，C01将碗平稳放到台面后收手，镜头固定。结束：成菜静置，厨师手已离开画面。

### S03：20—30秒

参考：F01完整成菜、E01台面；上传映射待填。品牌文案后期添加。

- 00:00—00:04：成菜近景，约30度俯拍，保留整个白碗，自然蒸汽，镜头轻推，背景不出现人脸；轻器皿声与音乐。
- 00:04—00:07：特写，面与清汤细节，固定镜头，食物不变形、不增添配菜；音乐准备收束；硬切。
- 00:07—00:10：中近景，成菜位于画面下半部，上方留干净负空间，停稳。视频不生成文字；后期在留白处添加“一碗热面”，声音自然收尾。

## 5. 总控记录与检查

|交付|状态|未验证项|
|---|---|---|
|需求与大纲|演示假设|没有真实用户阶段确认|
|资产设定与英文提示词|文字示例已编写|无图片、布局未确认|
|3段视频提示词|缺图草案|上传映射、实际动作、视频节奏|
|媒体与成片|未开始|未生成图片/视频/音乐，未剪辑|

三段各10秒，合计30秒。S01结束未加汤，S02完成成菜，S03展示品牌，动作状态衔接清楚；文本检查不能替代实际素材验收。

真实工作从阶段确认开始：先确认需求，再确认剧本清单及内容，生成并确认参考资产，最后填写真实上传映射并试拍重点片段。
