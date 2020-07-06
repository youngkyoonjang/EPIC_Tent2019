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

## Frame-by-fram action label ground truths

Frame-by-frame action label ground truths used for the online recognition section of the paper are contained in the frame_level_action_annotation directory.
Each participants has a file of the style: <ParcticipantNumber>.frame_level_gt.txt

The file contains 2 columns:
frame_digit -> Frame number in GoPro Video
action_id -> Action (sub-task) Label for that frame 


## Appendix: lables associated with index

Action_annotation = {0:'assemble support',   1:'insert stake',           2:'insert support',         3:'insert support tab',
                     4:'instruction',        5:'pickup/open stakebag',   6:'pickup/open supportbag', 7:'pickup/open tentbag',
                     8:'pickup/place ventcover', 9:'place guyline',      10:'spread tent',           11:'tie top'}
                            
Error_annotation = {0:'motor', 1:'misuse', 2:'order', 3:'failure', 4:'omit', 5:'search', 6:'correction', 7:'slow', 8:'repeat'}

## Appendix: note for error annotations

Note, begin time codes for Omit and Order error annotations denote time when the error began.

End time codes for omission should not be used as omission is the absence of an action.

Ordering errors timecodes denotes the begin and end of the ongoing action, but the ordering error is about going out of sequence not duration.
