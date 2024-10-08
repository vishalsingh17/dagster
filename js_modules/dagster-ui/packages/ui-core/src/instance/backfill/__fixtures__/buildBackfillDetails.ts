import {MockedResponse} from '@apollo/client/testing';

import {PartitionBackfill, buildPartitionBackfill} from '../../../graphql/types';
import {BackfillStatusesByAssetQuery} from '../types/useBackfillDetailsQuery.types';
import {BACKFILL_DETAILS_QUERY} from '../useBackfillDetailsQuery';

export function buildBackfillDetailsQuery(
  backfillId: string,
  partitionBackfill: Partial<PartitionBackfill>,
): MockedResponse<BackfillStatusesByAssetQuery> {
  return {
    request: {
      query: BACKFILL_DETAILS_QUERY,
      variables: {backfillId},
    },
    result: {
      data: {
        __typename: 'Query',
        partitionBackfillOrError: buildPartitionBackfill(partitionBackfill),
      },
    },
  };
}
