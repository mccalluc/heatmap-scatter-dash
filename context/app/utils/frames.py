import pandas


def merge(frames):
    """
    Given a list of frames, merge them, potentially creating new keys.
    """
    accumulator = pandas.DataFrame()
    for frame in frames:
        accumulator = accumulator.merge(
            frame,
            how='outer',
            right_index=True,
            left_index=True)
    return accumulator


def find_index(frame, keys, drop_unmatched=False):
    """
    Given a dataframe that came in with no explicit index,
    and a set of keys,
    identify a column whose values come from keys, and use that as the index.
    """
    for index, row in frame.iterrows():
        matches = []
        for column_name, value in row.to_dict().items():
            if value in keys:
                matches.append(column_name)
        if len(matches) == 1:
            break
        # Multiple matches or no matches: try the next row.
        # (No matches is possible because the frame may be truncated.)
    if len(matches) != 1:
        raise Exception(
            'No row where exactly one column matched keys: {}'.format(keys)
        )
    reindexed = frame.set_index(matches)
    # TODO: Remove this if not being used:
    # if drop_unmatched:
    #     unmatched_indexes = set(reindexed.index) - set(keys)
    #     reindexed.drop(unmatched_indexes, inplace=True)
    return reindexed


def sort_by_variance(frame):
    """
    Given a dataframe,
    reorder by variance, descending.
    """
    new_order = frame.var('columns').sort_values(ascending=False).index
    return frame.reindex(labels=new_order, axis='rows')
