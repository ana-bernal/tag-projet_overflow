def classif_report_per_tag(tag_list,y_test,y_pred):
    
    reports = {}

    for idx,tag in enumerate(tag_list):
        reports[tag] = classification_report(
            y_test.values[:,idx], 
            y_pred[:,idx], 
            target_names=[tag, f'not_{tag}'],
            output_dict=True)
    
    precision = [reports[rep]['macro avg']['precision'] for rep in reports]
    recall = [reports[rep]['macro avg']['recall'] for rep in reports]
    f1_score = [reports[rep]['macro avg']['f1-score'] for rep in reports]
    accuracy = [reports[rep]['accuracy'] for rep in reports]
    support = [reports[tag][tag]['support'] for tag in tag_list]
    support_not_tag = [reports[tag][f'not_{tag}']['support'] for tag in tag_list]

    report = pd.DataFrame({'tag': tag_list,
                           'precision': precision,
                           'recall' : recall,
                           'f1_score' : f1_score,
                           'accuracy' : accuracy, 
                           'support' : support, 
                           'support_not_tag' : support_not_tag
                           }
                          )
    
    avg_metrics = report[['precision', 'recall', 'f1_score', 'accuracy']].mean()

    return report, avg_metrics
