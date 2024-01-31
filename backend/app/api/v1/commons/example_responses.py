def response_200(example):
    return {
        "content": {
            "application/json": {
                "example": example,
            }
        },
    }


def response_422():
    return {
        "content": {
            "application/json": {
                "example": {"error": "invalid date format, start_date must be less than end_date"},
            }
        },
    }


ocp_response_example = {
    "startDate": "2023-09-20",
    "endDate": "2023-09-20",
    "results": [
        {
            "ciSystem": "PROW",
            "uuid": "CPT-e3865b03-ce78-454a-becb-b79aeb806a6b",
            "releaseStream": "4.14.0-0.nightly",
            "platform": "AWS",
            "clusterType": "self-managed",
            "benchmark": "cluster-density-v2",
            "masterNodesCount": 3,
            "workerNodesCount": 252,
            "infraNodesCount": 3,
            "masterNodesType": "m6a.8xlarge",
            "workerNodesType": "m5.2xlarge",
            "infraNodesType": "r5.4xlarge",
            "totalNodesCount": 258,
            "clusterName": "ci-op-4n0msnvp-7904a-s5sv8",
            "ocpVersion": "4.14.0-0.nightly-2023-09-15-233408",
            "networkType": "OVNKubernetes",
            "buildTag": "1704299395064795136",
            "jobStatus": "success",
            "buildUrl": "https://example.com/1704299395064795136",
            "upstreamJob": "periodic-ci-openshift",
            "upstreamJobBuild": "5fe07ad3-5415-433c-b9af-f60545d0d432",
            "executionDate": "2023-09-20T02:14:07Z",
            "jobDuration": "5261",
            "startDate": "2023-09-20T02:14:07Z",
            "endDate": "2023-09-20T03:41:48Z",
            "timestamp": "2023-09-20T02:14:07Z",
            "shortVersion": "4.14"
        },
        {
            "ciSystem": "PROW",
            "uuid": "CPT-0d58dddf-721a-4952-985e-046bc17ee3cc",
            "releaseStream": "4.13.0-0.nightly",
            "platform": "GCP",
            "clusterType": "self-managed",
            "benchmark": "node-density",
            "masterNodesCount": 3,
            "workerNodesCount": 24,
            "infraNodesCount": 3,
            "masterNodesType": "e2-standard-4",
            "workerNodesType": "e2-standard-4",
            "infraNodesType": "n1-standard-16",
            "totalNodesCount": 30,
            "clusterName": "ci-op-x2ic4nsf-8360f-kzbcg",
            "ocpVersion": "4.13.0-0.nightly-2023-09-12-074803",
            "networkType": "OVNKubernetes",
            "buildTag": "1704367060252889088",
            "jobStatus": "success",
            "buildUrl": "https://example/1704367060252889088",
            "upstreamJob": "periodic-ci-openshift",
            "upstreamJobBuild": "3ab02e3b-3000-4fc9-a30c-9cd02fe4a78c",
            "executionDate": "2023-09-20T07:19:00Z",
            "jobDuration": "582",
            "startDate": "2023-09-20T07:19:00Z",
            "endDate": "2023-09-20T07:28:42Z",
            "timestamp": "2023-09-20T07:19:00Z",
            "shortVersion": "4.13"
        },
    ]
}


def ocp_200_response():
    return response_200(ocp_response_example)


cpt_response_example = {
    "startDate": "2023-11-18",
    "endDate": "2023-11-23",
    "results": [
        {
            "ciSystem": "PROW",
            "uuid": "f6d084d5-b154-4108-b4f7-165094ccc838",
            "releaseStream": "Nightly",
            "jobStatus": "success",
            "buildUrl": "https://ci..org/view/1726571333392797696",
            "startDate": "2023-11-20T13:16:34Z",
            "endDate": "2023-11-20T13:28:48Z",
            "product": "ocp",
            "version": "4.13",
            "testName": "cluster-density-v2"
        },
        {
            "ciSystem": "JENKINS",
            "uuid": "5b729011-3b4d-4ec4-953d-6881ac9da505",
            "releaseStream": "Stable",
            "jobStatus": "success",
            "buildUrl": "https://ci..org/view/1726571333392797696",
            "startDate": "2023-11-20T13:16:30Z",
            "endDate": "2023-11-20T13:30:40Z",
            "product": "ocp",
            "version": "4.14",
            "testName": "node-density-heavy"
        },
    ]
}


def cpt_200_response():
    return response_200(cpt_response_example)


stub_results_example = {
    "results": [
        {
            "ciSystem": "PROW",
            "uuid": "730debd8-7fff-48d4-9ea6-e6286dace207",
            "releaseStream": "4.12.47",
            "platform": "AWS ROSA",
            "clusterType": "rosa",
            "benchmark": "upgrade-cluster-density-v2",
            "masterNodesCount": 3,
            "workerNodesCount": 24,
            "infraNodesCount": 3,
            "masterNodesType": "m5.2xlarge",
            "workerNodesType": "m5.xlarge",
            "infraNodesType": "r5.xlarge",
            "totalNodesCount": 30,
            "clusterName": "ci-rosa-s-a7f4-rhb6c",
            "ocpVersion": "4.12.47",
            "networkType": "OVNKubernetes",
            "buildTag": "1749433137986801664",
            "jobStatus": "success",
            "buildUrl": "https://ci.org/view/gs/origin-ci-test/logs/rehearse-47677-periodic-ci-openshift-qe-ocp-qe-perfscale-ci-main-rosa-4.14-candidate-x86-loaded-upgrade-from-4.12-perfscale-rosa-multiaz-24nodes-stage-loaded-upgrade414/1749433137986801664",
            "upstreamJob": "rehearse-47677-periodic-ci-openshift-qe-ocp-qe-perfscale-ci-main-rosa-4.14-candidate-x86-loaded-upgrade-from-4.12-perfscale-rosa-multiaz-24nodes-stage-loaded-upgrade414",
            "upstreamJobBuild": "5fa34a7f-423b-4ffa-970a-6239b95a7c54",
            "executionDate": "2024-01-22T15:11:29Z",
            "jobDuration": "499",
            "startDate": "2024-01-22T15:11:29Z",
            "endDate": "2024-01-22T15:19:48Z",
            "startDateUnixTimestamp": "1705936289",
            "endDateUnixTimestamp": "1705936788",
            "timestamp": "2024-01-22T15:11:29Z",
            "ipsec": "false",
            "fips": "false",
            "encrypted": "true",
            "encryptionType": "aescbc",
            "publish": "External",
            "computeArch": "amd64",
            "controlPlaneArch": "amd64",
            "jobType": "periodic",
            "isRehearse": "True",
            "build": "4.12.47",
            "shortVersion": "4.12"
        },
        {
            "ciSystem": "PROW",
            "uuid": "e34ef8d5-cfc3-433b-a1e0-db06da1412ab",
            "releaseStream": "4.15.0-0.nightly",
            "platform": "VSphere",
            "clusterType": "self-managed",
            "benchmark": "cluster-density-v2",
            "masterNodesCount": 3,
            "workerNodesCount": 24,
            "infraNodesCount": 3,
            "masterNodesType": "vsphere-vm.cpu-4.mem-16gb.os-unknown",
            "workerNodesType": "vsphere-vm.cpu-4.mem-16gb.os-unknown",
            "infraNodesType": "vsphere-vm.cpu-16.mem-64gb.os-unknown",
            "totalNodesCount": 30,
            "clusterName": "ci-op-fg6pyq0w-46dbc-q5z9n",
            "ocpVersion": "4.15.0-0.nightly-2024-01-18-050837",
            "networkType": "OVNKubernetes",
            "buildTag": "1749328983566061568",
            "jobStatus": "success",
            "buildUrl": "https://ci.org/view/gs/origin-ci-test/logs/rehearse-47635-pull-ci-openshift-qe-ocp-qe-perfscale-ci-main-vsphere-4.15-nightly-x86-control-plane-24nodes/1749328983566061568",
            "upstreamJob": "rehearse-47635-pull-ci-openshift-qe-ocp-qe-perfscale-ci-main-vsphere-4.15-nightly-x86-control-plane-24nodes",
            "upstreamJobBuild": "fd70ce91-51e1-43d0-ba21-b346b8fe884f",
            "executionDate": "2024-01-22T08:23:44Z",
            "jobDuration": "2694",
            "startDate": "2024-01-22T08:23:44Z",
            "endDate": "2024-01-22T09:08:38Z",
            "startDateUnixTimestamp": "1705911824",
            "endDateUnixTimestamp": "1705914518",
            "timestamp": "2024-01-22T08:23:44Z",
            "ipsec": "false",
            "fips": "false",
            "encrypted": "false",
            "encryptionType": "None",
            "publish": "External",
            "computeArch": "amd64",
            "controlPlaneArch": "amd64",
            "jobType": "pull request",
            "isRehearse": "True",
            "build": "2024-01-18-050837",
            "shortVersion": "4.15"
        },
        {
            "ciSystem": "PROW",
            "uuid": "fa77697a-224a-4f03-9b04-e9036f914286",
            "releaseStream": "4.13.0-0.nightly",
            "platform": "GCP",
            "clusterType": "self-managed",
            "benchmark": "node-density-cni",
            "masterNodesCount": 3,
            "workerNodesCount": 24,
            "infraNodesCount": 3,
            "masterNodesType": "e2-custom-6-16384",
            "workerNodesType": "e2-standard-4",
            "infraNodesType": "n1-standard-16",
            "totalNodesCount": 30,
            "clusterName": "ci-op-zlxq07vd-4a3a0-m9fdq",
            "ocpVersion": "4.13.0-0.nightly-2024-01-20-234646",
            "networkType": "OVNKubernetes",
            "buildTag": "1749401600893390848",
            "jobStatus": "success",
            "buildUrl": "https://ci.org/view/gs/origin-ci-test/logs/periodic-ci-openshift-qe-ocp-qe-perfscale-ci-main-gcp-4.13-nightly-x86-node-density-cni-24nodes/1749401600893390848",
            "upstreamJob": "periodic-ci-openshift-qe-ocp-qe-perfscale-ci-main-gcp-4.13-nightly-x86-node-density-cni-24nodes",
            "upstreamJobBuild": "276e0ff6-a30a-4553-87b2-d8ba4cca4208",
            "executionDate": "2024-01-22T13:02:24Z",
            "jobDuration": "612",
            "startDate": "2024-01-22T13:02:24Z",
            "endDate": "2024-01-22T13:12:36Z",
            "startDateUnixTimestamp": "1705928544",
            "endDateUnixTimestamp": "1705929156",
            "timestamp": "2024-01-22T13:02:24Z",
            "ipsec": "false",
            "fips": "false",
            "encrypted": "false",
            "encryptionType": "None",
            "publish": "External",
            "computeArch": "amd64",
            "controlPlaneArch": "amd64",
            "jobType": "periodic",
            "isRehearse": "False",
            "build": "2024-01-20-234646",
            "shortVersion": "4.13"
        },
        {
            "ciSystem": "PROW",
            "uuid": "009482dc-171b-4b57-95bf-c0af97474194",
            "releaseStream": "4.14.0-0.nightly",
            "platform": "AWS",
            "clusterType": "self-managed",
            "benchmark": "k8s-netperf",
            "masterNodesCount": 3,
            "workerNodesCount": 9,
            "infraNodesCount": 3,
            "masterNodesType": "m6g.xlarge",
            "workerNodesType": "m6g.xlarge",
            "infraNodesType": "m6g.8xlarge",
            "totalNodesCount": 15,
            "clusterName": "ci-op-4z7fvgz0-6acc1-7dj7g",
            "ocpVersion": "4.14.0-0.nightly-arm64-2024-01-20-231147",
            "networkType": "OVNKubernetes",
            "buildTag": "1748948617030275072",
            "jobStatus": "success",
            "buildUrl": "https://ci.org/view/gs/origin-ci-test/logs/periodic-ci-openshift-qe-ocp-qe-perfscale-ci-main-aws-4.14-nightly-arm-data-path-9nodes/1748948617030275072",
            "upstreamJob": "periodic-ci-openshift-qe-ocp-qe-perfscale-ci-main-aws-4.14-nightly-arm-data-path-9nodes",
            "upstreamJobBuild": "5052c6a1-11f1-423d-a38b-638ca440bafd",
            "executionDate": "2024-01-21T07:16:00Z",
            "jobDuration": "7706",
            "startDate": "2024-01-21T07:16:00Z",
            "endDate": "2024-01-21T09:24:26Z",
            "startDateUnixTimestamp": "1705821360",
            "endDateUnixTimestamp": "1705829066",
            "timestamp": "2024-01-21T07:16:00Z",
            "ipsec": "false",
            "fips": "false",
            "encrypted": "false",
            "encryptionType": "None",
            "publish": "External",
            "computeArch": "arm64",
            "controlPlaneArch": "arm64",
            "jobType": "periodic",
            "isRehearse": "False",
            "build": "arm64-2024-01-20-231147",
            "shortVersion": "4.14"
        },
        {
            "ciSystem": "PROW",
            "uuid": "ec5a438c-8d22-4307-bde0-e6dca641dc50",
            "releaseStream": "4.15.0-0.nightly",
            "platform": "AWS",
            "clusterType": "self-managed",
            "benchmark": "ingress-perf",
            "masterNodesCount": 3,
            "workerNodesCount": 9,
            "infraNodesCount": 3,
            "masterNodesType": "m6g.xlarge",
            "workerNodesType": "m6g.xlarge",
            "infraNodesType": "m6g.8xlarge",
            "totalNodesCount": 15,
            "clusterName": "ci-op-ixtnmvj6-1633c-87lm8",
            "ocpVersion": "4.15.0-0.nightly-arm64-2024-01-21-010454",
            "networkType": "OVNKubernetes",
            "buildTag": "1749356301592301568",
            "jobStatus": "success",
            "buildUrl": "https://ci.org/view/gs/origin-ci-test/logs/periodic-ci-openshift-qe-ocp-qe-perfscale-ci-main-aws-4.15-nightly-arm-data-path-9nodes/1749356301592301568",
            "upstreamJob": "periodic-ci-openshift-qe-ocp-qe-perfscale-ci-main-aws-4.15-nightly-arm-data-path-9nodes",
            "upstreamJobBuild": "3cb1ed44-1f69-40fd-bb63-1523f168d39e",
            "executionDate": "2024-01-22T12:27:28Z",
            "jobDuration": "2537",
            "startDate": "2024-01-22T12:27:28Z",
            "endDate": "2024-01-22T13:09:45Z",
            "startDateUnixTimestamp": "1705926448",
            "endDateUnixTimestamp": "1705928985",
            "timestamp": "2024-01-22T12:27:28Z",
            "ipsec": "false",
            "fips": "false",
            "encrypted": "false",
            "encryptionType": "None",
            "publish": "External",
            "computeArch": "arm64",
            "controlPlaneArch": "arm64",
            "jobType": "periodic",
            "isRehearse": "False",
            "build": "arm64-2024-01-21-010454",
            "shortVersion": "4.15"
        },
        {
            "ciSystem": "PROW",
            "uuid": "a3ab7f88-c55c-4be8-a2f8-e8ebf0f20ed1",
            "releaseStream": "4.14.0-ec.4",
            "platform": "AWS ROSA",
            "clusterType": "rosa",
            "benchmark": "k8s-netperf",
            "masterNodesCount": 3,
            "workerNodesCount": 9,
            "infraNodesCount": 3,
            "masterNodesType": "m5.2xlarge",
            "workerNodesType": "m5.xlarge",
            "infraNodesType": "r5.xlarge",
            "totalNodesCount": 15,
            "clusterName": "ci-rosa-s-88b6-l5zxz",
            "ocpVersion": "4.14.0-ec.4",
            "networkType": "OVNKubernetes",
            "buildTag": "1749356302443745280",
            "jobStatus": "success",
            "buildUrl": "https://ci.org/view/gs/origin-ci-test/logs/periodic-ci-openshift-qe-ocp-qe-perfscale-ci-main-rosa-4.14-ec-x86-data-path-9nodes/1749356302443745280",
            "upstreamJob": "periodic-ci-openshift-qe-ocp-qe-perfscale-ci-main-rosa-4.14-ec-x86-data-path-9nodes",
            "upstreamJobBuild": "25ab06ef-f6b3-4f15-a7f6-56bed4cd8f72",
            "executionDate": "2024-01-22T10:19:00Z",
            "jobDuration": "7711",
            "startDate": "2024-01-22T10:19:00Z",
            "endDate": "2024-01-22T12:27:31Z",
            "startDateUnixTimestamp": "1705918740",
            "endDateUnixTimestamp": "1705926451",
            "timestamp": "2024-01-22T10:19:00Z",
            "ipsec": "false",
            "fips": "false",
            "encrypted": "true",
            "encryptionType": "aescbc",
            "publish": "External",
            "computeArch": "amd64",
            "controlPlaneArch": "amd64",
            "jobType": "periodic",
            "isRehearse": "False",
            "build": "4.14.0-ec.4",
            "shortVersion": "4.14"
        },
        {
            "ciSystem": "PROW",
            "uuid": "d1481b67-1978-420e-bbeb-3eb3675d0c7f",
            "releaseStream": "4.14.0-ec.4",
            "platform": "AWS ROSA",
            "clusterType": "rosa",
            "benchmark": "cluster-density-v2",
            "masterNodesCount": 3,
            "workerNodesCount": 24,
            "infraNodesCount": 3,
            "masterNodesType": "m5.2xlarge",
            "workerNodesType": "",
            "infraNodesType": "r5.xlarge",
            "totalNodesCount": 30,
            "clusterName": "ci-rosa-s-6fff-8sm9n",
            "ocpVersion": "4.14.0-ec.4",
            "networkType": "OVNKubernetes",
            "buildTag": "1749401605884612608",
            "jobStatus": "success",
            "buildUrl": "https://ci.org/view/gs/origin-ci-test/logs/periodic-ci-openshift-qe-ocp-qe-perfscale-ci-main-rosa-4.14-ec-x86-control-plane-24nodes/1749401605884612608",
            "upstreamJob": "periodic-ci-openshift-qe-ocp-qe-perfscale-ci-main-rosa-4.14-ec-x86-control-plane-24nodes",
            "upstreamJobBuild": "ef1d235e-4952-4a24-81a2-2cd0703b6dc7",
            "executionDate": "2024-01-22T12:56:51Z",
            "jobDuration": "2069",
            "startDate": "2024-01-22T12:56:51Z",
            "endDate": "2024-01-22T13:31:20Z",
            "startDateUnixTimestamp": "1705928211",
            "endDateUnixTimestamp": "1705930280",
            "timestamp": "2024-01-22T12:56:51Z",
            "ipsec": "false",
            "fips": "false",
            "encrypted": "true",
            "encryptionType": "aescbc",
            "publish": "External",
            "computeArch": "amd64",
            "controlPlaneArch": "amd64",
            "jobType": "periodic",
            "isRehearse": "False",
            "build": "4.14.0-ec.4",
            "shortVersion": "4.14"
        },
        {
            "ciSystem": "JENKINS",
            "uuid": "da34a989-60cc-4537-baae-7fd10e6bee22",
            "releaseStream": "4.15.0-0.nightly",
            "platform": "AWS",
            "clusterType": "self-managed",
            "benchmark": "node-density-heavy",
            "masterNodesCount": 3,
            "workerNodesCount": 25,
            "infraNodesCount": 0,
            "masterNodesType": "m6i.4xlarge",
            "workerNodesType": "m6i.4xlarge",
            "infraNodesType": "",
            "totalNodesCount": 28,
            "clusterName": "noci-18-mzz66",
            "ocpVersion": "4.15.0-0.nightly-2024-01-18-050837",
            "networkType": "OVNKubernetes",
            "buildTag": "901",
            "jobStatus": "success",
            "buildUrl": "https://jenkins.com/job/scale-ci/job/e2e-benchmarking-multibranch-pipeline/job/kube-burner-ocp/901/",
            "upstreamJob": "kube-burner-ocp",
            "upstreamJobBuild": "",
            "executionDate": "2024-01-22T11:12:51Z",
            "jobDuration": "643",
            "startDate": "2024-01-22T11:12:51Z",
            "endDate": "2024-01-22T11:23:34Z",
            "startDateUnixTimestamp": "1705921971",
            "endDateUnixTimestamp": "1705922614",
            "timestamp": "2024-01-22T11:12:51Z",
            "ipsec": "false",
            "fips": "false",
            "encrypted": "false",
            "encryptionType": "None",
            "publish": "External",
            "computeArch": "amd64",
            "controlPlaneArch": "amd64",
            "jobType": "pull request",
            "isRehearse": "False",
            "build": "2024-01-18-050837",
            "shortVersion": "4.15"
        },
        {
            "ciSystem": "JENKINS",
            "uuid": "4572ad33-be27-49b1-9d0e-db71bb1446bb",
            "releaseStream": "4.14.10",
            "platform": "GCP",
            "clusterType": "self-managed",
            "benchmark": "cluster-density-v2",
            "masterNodesCount": 3,
            "workerNodesCount": 20,
            "infraNodesCount": 0,
            "masterNodesType": "n2-standard-4",
            "workerNodesType": "n1-standard-4",
            "infraNodesType": "",
            "totalNodesCount": 23,
            "clusterName": "load-up413-2206-785wx",
            "ocpVersion": "4.14.10",
            "networkType": "OVNKubernetes",
            "buildTag": "900",
            "jobStatus": "success",
            "buildUrl": "https://jenkins.com/job/scale-ci/job/e2e-benchmarking-multibranch-pipeline/job/kube-burner-ocp/900/",
            "upstreamJob": "kube-burner-ocp",
            "upstreamJobBuild": "",
            "executionDate": "2024-01-22T01:59:51Z",
            "jobDuration": "1352",
            "startDate": "2024-01-22T01:59:51Z",
            "endDate": "2024-01-22T02:22:23Z",
            "startDateUnixTimestamp": "1705888791",
            "endDateUnixTimestamp": "1705890143",
            "timestamp": "2024-01-22T01:59:51Z",
            "ipsec": "false",
            "fips": "false",
            "encrypted": "false",
            "encryptionType": "None",
            "publish": "External",
            "computeArch": "amd64",
            "controlPlaneArch": "amd64",
            "jobType": "pull request",
            "isRehearse": "False",
            "build": "4.14.10",
            "shortVersion": "4.14"
        },
        {
            "ciSystem": "PROW",
            "uuid": "012e62a4-0523-46f2-bd56-de082d7193a7",
            "releaseStream": "4.14.0-0.nightly",
            "platform": "AWS ROSA",
            "clusterType": "rosa",
            "benchmark": "node-density-heavy",
            "masterNodesCount": 3,
            "workerNodesCount": 24,
            "infraNodesCount": 3,
            "masterNodesType": "m5.2xlarge",
            "workerNodesType": "m5.xlarge",
            "infraNodesType": "r5.xlarge",
            "totalNodesCount": 30,
            "clusterName": "ci-rosa-s-a8f0-qbtnv",
            "ocpVersion": "4.14.0-0.nightly-2024-01-23-102424",
            "networkType": "OVNKubernetes",
            "buildTag": "1749760234089353216",
            "jobStatus": "success",
            "buildUrl": "https://ci.org/view/gs/origin-ci-test/logs/rehearse-47827-periodic-ci-openshift-qe-ocp-qe-perfscale-ci-main-rosa-4.14-nightly-x86-node-density-heavy-24nodes/1749760234089353216",
            "upstreamJob": "rehearse-47827-periodic-ci-openshift-qe-ocp-qe-perfscale-ci-main-rosa-4.14-nightly-x86-node-density-heavy-24nodes",
            "upstreamJobBuild": "ece417d8-ece2-4148-964c-69c2114e239c",
            "executionDate": "2024-01-23T12:50:42Z",
            "jobDuration": "2516",
            "startDate": "2024-01-23T12:50:42Z",
            "endDate": "2024-01-23T13:32:38Z",
            "startDateUnixTimestamp": "1706014242",
            "endDateUnixTimestamp": "1706016758",
            "timestamp": "2024-01-23T12:50:42Z",
            "ipsec": "false",
            "fips": "false",
            "encrypted": "true",
            "encryptionType": "aescbc",
            "publish": "External",
            "computeArch": "amd64",
            "controlPlaneArch": "amd64",
            "jobType": "periodic",
            "isRehearse": "True",
            "build": "2024-01-23-102424",
            "shortVersion": "4.14"
        },
    ]}


def stub_results():
    return stub_results_example


def stub_columns():
    return {
        'benchmark': 'Benchmark',
        'releaseStream': 'Release Stream',
        'build': 'Build',
        'workerNodesCount': 'Worker Count',
        'startDate': 'Start Date',
        'endDate': 'End Date',
        'jobStatus': 'Status'
    }


def stub_filters():
    return {
        'ciSystem': 'Ci System',
        'platform': 'Platform',
        'benchmark': 'Benchmark',
        'workerNodesCount': 'Workers Count',
        'networkType': 'Network Type',
        'shortVersion': 'Versions',
        'jobType': 'Job Type',
        'isRehearse': 'Rehearse',
        'ipsec': 'Has IPSEC',
        'fips': 'FIPS Enabled',
        'encrypted': 'Is Encrypted',
        'encryptionType': 'Encryption Type',
        'publish': 'Control Plane Access',
        'computeArch': 'Compute Architecture',
        'controlPlaneArch': 'Control Plane Architecture'
    }
