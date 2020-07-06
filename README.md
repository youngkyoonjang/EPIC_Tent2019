# EPIC_Tent2019
EPIC_Tent2019 annotation

Each video has a different frame rate. The annotation files provide a synchronized timestamp between videos.

<root folder>/Synchronised_action_label.txt

Columns correspond to:
1) subject_id <- Subject ID
2) str_GoPro_ts <- Begin GoPro Timecode
3) end_GoPro_ts <- End GoPro Timecode
4) str_GoPro_frame <- Begin GoPro Frame Index
5) end_GoPro_frame <- End GoPro Frame Index
6) str_SMI_w_ts <- Begin SMI with eye Timecode
7) end_SMI_w_ts <- End SMI with eye Timecode
8) str_SMI_w_frame <- Begin SMI with eye Frame Index
9) end_SMI_w_frame <- End SMI with eye Frame Index
10) str_SMI_wo_ts <- Begin SMI without eye Timecode
11) end_SMI_wo_ts <- End SMI without eye Timecode
12) str_SMI_wo_frame <- Begin SMI without eye Frame Index
13) end_SMI_wo_frame <- End SMI without eye Frame Index
14) action_label <- Action (Subtask) Label

<root folder>/Synchronised_error_label.txt

1) subject_id <- Subject ID
2) str_GoPro_ts <- Begin GoPro Timecode
3) end_GoPro_ts <- End GoPro Timecode
4) str_GoPro_frame <- Begin GoPro Frame Index
5) end_GoPro_frame <- End GoPro Frame Index
6) str_SMI_w_ts <- Begin SMI with eye Timecode
7) end_SMI_w_ts <- End SMI with eye Timecode
8) str_SMI_w_frame <- Begin SMI with eye Frame Index
9) end_SMI_w_frame <- End SMI with eye Frame Index
10) str_SMI_wo_ts <- Begin SMI without eye Timecode
11) end_SMI_wo_ts <- End SMI without eye Timecode
12) str_SMI_wo_frame <- Begin SMI without eye Frame Index
13) end_SMI_wo_frame <- End SMI without eye Frame Index
14) error_label_main <- Error Label
15) error_label_sub <- (concurrent) Error Label (-1 represents no concurrent error label)
16) action_label <- Action (Subtask) Label associated with Action Segment
