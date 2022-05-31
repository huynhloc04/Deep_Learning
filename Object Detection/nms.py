
import torch
from IoU import intersection_over_union


def nms(bboxes, iou_threshold, probs_threshold):
    assert type(bboxes) == list()

    """"
    box is a list [class, probs_pred, x1, y1, x2, y2]
    """
    bboxes = [box for box in bboxes if box[1] >= probs_threshold]
    bboxes = sorted(bboxes, key = lambda x : x[1], reverse = True)
    bboxes_after_nms = []

    while bboxes:
        chosen_box = bboxes.pop(0)
        bboxes = [box for box in bboxes
                        if box[0] != chosen_box[0] or intersection_over_union(
                                                                    torch.tensor(box[2:]), 
                                                                    torch.tensor(chosen_box[2:]) < iou_threshold)]
        bboxes_after_nms.append(chosen_box)
    
    return bboxes_after_nms

